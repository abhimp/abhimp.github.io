/* Light/dark theme toggle.
   The initial theme class is added to <html> by an inline boot script in
   head.html (before first paint). This file wires the toggle control and keeps
   its icon in sync.

   The control is identified by href="#toggle-theme" (NOT by id), because the
   template's mobile menu (util.js navList) rebuilds the nav links and drops the
   id — only href/target/text survive. The click listener runs in the CAPTURE
   phase so it fires before the mobile panel's handler (main.js, hideOnClick)
   calls stopPropagation(). */
(function () {
	var SELECTOR = 'a[href="#toggle-theme"]';

	function currentTheme() {
		return document.documentElement.classList.contains('dark') ? 'dark' : 'light';
	}

	function syncIcon() {
		// Show the theme you'd switch TO: moon while light, sun while dark.
		var icon = currentTheme() === 'dark' ? '☀' : '☾'; // ☀ / ☾
		var btns = document.querySelectorAll(SELECTOR);
		for (var i = 0; i < btns.length; i++) {
			var b = btns[i];
			// Preserve the indent <span> the mobile panel injects; replace text.
			var span = b.querySelector('span');
			while (b.firstChild) b.removeChild(b.firstChild);
			if (span) b.appendChild(span);
			b.appendChild(document.createTextNode(icon));
		}
	}

	function toggleTheme() {
		var el = document.documentElement;
		var dark = el.classList.toggle('dark');
		el.classList.toggle('light', !dark);
		try { localStorage.setItem('theme', dark ? 'dark' : 'light'); } catch (_) {}
		syncIcon();
	}

	// Capture phase: beats the mobile panel's stopPropagation() and dropotron.
	document.addEventListener('click', function (e) {
		var t = e.target;
		var a = t && t.closest ? t.closest(SELECTOR) : null;
		if (!a) return;
		e.preventDefault();
		e.stopPropagation();
		toggleTheme();
		// If tapped from the mobile slide-in menu, close it.
		document.body.classList.remove('navPanel-visible');
	}, true);

	document.addEventListener('DOMContentLoaded', syncIcon);
})();
