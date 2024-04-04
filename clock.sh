

x1=" .---.     .  ---.  ---. .   . .---  .---   ---. .---. .---. .---."
x2=" |   |     |     |     | |   | |     |         | |   | |   | |   |"
x3=" |   |     | .---   ---| \`---| '---. |---.     | |---| \`---| |   |"
x4=" |   |     | |         |     |     | |   |     | |   |     | |   |"
x5=" '---'     ' '---   ---'     '  ---' \`---'     ' '---'  ---' '---'"

dot="  o o "

boxSize=47


clock() {
    cnt=$1
    dot="  o o "
    if [[ "$cnt" == "0" ]]; then
        dot="      "
    fi
    tm=$(date +%I:%M:%S)
    #echo $tm
    am_pm=$(date +"%p")
    frontBuffer=$((COLUMNS - boxSize))
    frontBuffer=$((frontBuffer / 2))
    skips=$((LINES - 7))
    skips=$((skips / 2))
    for i in `seq 2 $skips`; do
        echo ""
    done

    printf '%*s%s %s\n' $frontBuffer '' $tm $am_pm

    printf '%*s' $frontBuffer ''
    printf '+'
    for x in `seq 1 $boxSize`; do
        printf '-'
    done
    printf '+\n'

    for j in {1..5}; do
        printf '%*s| ' $frontBuffer ''
        v=x$j
        st="${!v}"
        for (( i=0; i<${#tm}; i++)); do
            font="${tm:i:1}"
            if [[ "$font" == ":" ]]; then
                printf "%s" " ${dot:j:1} "
            else
                start=$((font * 6))
#                 echo $font $start
                printf "%s" "${st:start:6}"
            fi
        done
        if [[ "$j" == "5" ]]; then
            printf " %s" $am_pm
        else
            printf "   "
        fi
        printf " |"
        echo ""
    done

    printf '%*s' $frontBuffer ''
    printf '+'
    for x in `seq 1 $boxSize`; do
        printf '-'
    done
    printf '+\n'

    for i in `seq 1 $skips`; do
        echo "   "
    done
}

cnt=0

while true
do
    cnt=$((1 - cnt))
    pop="$(clock $cnt)"
    printf "%s" "$pop"
    sleep .5
done
