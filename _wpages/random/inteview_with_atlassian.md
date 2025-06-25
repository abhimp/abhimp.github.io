---
layout: blog
title: Openssl and single threaded application
menutype: blog
menu_order: 20
plink: interview_with_atlassian_backend_engineer
---

# Atlassian Interview
25-June-2025

I have been jobless since April 8th and am actively searching for a job. My preference is full-time remote work; however, there are very few options available in the remote space. As a result, I have not received many calls. Recently, I received a call from Atlassian. I would love to get an opportunity to work with Atlassian, but I think it is a long shot. Anyway, I am giving my interviews my best effort. Atlassian has multiple stages. I am writing about each stage of my interviews.

## Stage-1: Karat Interview

This is the first stage, where the interview is conducted by a third-party platform called Karat. The interview is held on Karat Studio. The interview is very tightly packed and has a strict schedule. My interview schedule was as follows:

1. 10 min introduction. The interviewer told me that he had taken around 500 interviews in the last 4 years. His primary job is taking interviews.
1. 15 min for 5 system questions. There is no drawing required. Everything is mostly verbal or written in the studio.
    * They provide some scenarios and ask for pros and cons.
    * They provide some scenarios with a problem and ask for a solution.
    * They simply ask to design a system.

    Most of the questions were pretty simple and straightforward.

1. 30 min coding.

    The interviewer did not say anything about the number of questions or anything like that. He just provided a problem and asked me to solve it. I chose Python to solve the problem. They allow candidates to check manuals on the Internet. I needed it to check some syntax in the Python documentation.

    1. The first problem was to find a superset from a list. There was a list of words, and given a word, find all the words from the word list from which we can create the provided word, i.e., all the letters (with their frequency) are present in the list.

        For example, if the list of words is `["acat", "acrobat", "foocat"]` and the provided word is `"caat"`, the output would be `["acat", "acrobat"]`.

        The problem was easy enough. However, due to a small mistake, I took 17 minutes to solve it. All the test cases passed without any issue.

    1. As I had about 13 minutes left, he gave me another problem. I thought there was no way I could solve this problem. The problem was to find a provided word in a 2D matrix of characters.

        I solved this problem; however, 1 test case did not pass. I had no time to debug it. So, the interviewer concluded the coding session there.
1. The last 5 minutes were left to conclude the interview. He just asked me if I had any questions and told me to provide honest feedback.

I was happy with the interview. However, I did not have any hope about the next steps, as I read on the Internet that this stage is extremely hard and most people did not pass even after acing the interview.

My Karat interview was at 3 PM on a Friday. I did not get any call for quite a few days. In the meantime, I faced a health issue as I developed extreme back pain due to my condition with PIVD and got severe allergies as a side effect of painkillers. While I was suffering from this, I got an email from the interview coordinator regarding my next stage.

## Stage-2: Coding Interview

The next stage is the coding interview. It consists of two interviews: a) Code-Design interview and b) Data Structure and Algorithm interview. I scheduled the interviews for two consecutive days. Each interview lasted for 1 hour. For both interviews, they asked me to keep my setup ready with my preferred IDE, preferred tooling, and Zoom.

### Stage-2.1: Coding Interview: Code-Design

The Code-Design interview is a special interview where the interviewer checks the code quality. It expects the following things:
1. Code quality: Code should be
    * Easy to understand
    * Easy to extend
    * Easy to test
2. Adaptability
    * Easy to adapt to changed requirements
3. Computer Science Concepts
    * Exceptions
    * Test cases
4. Rationality
    * All decisions while coding need to be rational
5. Resourcefulness
    * Use of resources to get ideas

After the initial introduction, the interviewer described the problem. Initially, they provided very few bits of the problem. I asked a ton of questions, and he revealed more parts of the problem. He was expecting TDD. I had never developed anything with TDD before. However, as I started writing code, I understood how easy it is to get confident in the code once I have TDD.

The initial problem was as follows: Write a Cost Explorer. Basically, a product has different packages, and users want to know the cost for a year. The problem is extremely simple, but TDD makes it time-consuming to develop. Anyway, once I completed this task, the interviewer extended it to provide estimation only to the end of the calendar year. I extended it. However, time was almost up, so the interviewer asked a few follow-up questions. The interview was good. I am satisfied as I have learned something.

### Stage-2.2: Coding Interview: Data Structure and Algorithm
The next day was the traditional Data Structure and Algorithm coding round. The interviewer provided me with the problem with minimal information. I asked several questions and finally understood that the problem was about `finding the closest parent of two or more nodes`. The problem itself is very easy; however, it took time to write auxiliary code and a little time to debug. I finished it in time. He did not ask me any follow-up questions. I am kind of disappointed with this interview.

The second interview was easy; however, I think I may have asked too many questions, which led to diluting the problem that I solved.

The interview coordinator might call back next week.