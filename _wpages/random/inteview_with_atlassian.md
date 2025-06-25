---
layout: blog
title: Openssl and single threaded application
menutype: blog
menu_order: 20
plink: interview_with_atlassian_backend_engineer
---

# Atlassian Interview
25-June-2025

I am jobless from last 8th April and I am actively searching for job. My preference is full time remote, however, there are very little option available in the remote space. So, I have not received lot of calls. Recently I received call from Altassain. I would love to get an opportunity to work with Atlassian, however, I think is it long shot. Anyway I am giving my interviews to my best. Atlassian has multiple stages. I am writing each stages of my interviews.

## Stag-1: Karat Interview

This is the first stage where interview is taken by third party platform call Karat. The interview is held on Karat studio. The interview is very tightly packed and have tight schedules: My interview schedule was as follows:

1. 10 min introduction. The interviewer told me that he tool around 500 interview in last 4 years. His primary job is taking interview.
1. 15 min for 5 system questions. They are no drawing required. Everything is mostly verbal or writing in the studio.
    * They provide some scenarios and ask pros and cons
    * They provide some scenarios with some problem and ask solution
    * They simply ask to design a system

    Most of the questions was pretty simple and straight forward

1. 30 min coding.

    Interviewer did not say anything about the no of questions or anything like that. Just provided a problem and asked me to solve it. I choose python to solve the problem. They allow candidate to check manuals in the Internet. I needed it to check some syntax in Python documentation.

    1. First problem was to find super set from a list. There was a list of words and provided a word, find all the words from word list from which we can create the provided word i.e. all the letter (with there frequency) are present in the list.

        For example the list of words is `["acat", "acrobat", "foocat"]` and the provided word is `"caat"`, output would be `["acat", "acrobat"]`.

        The problem is easy enough. However, due a small mistake, I took 17 minutes to solve it. All the test cases passed without any issue.

    1. As I had about 13 minutes, he gave me another problem. I thought, there is no way I can solve this problem. The problem was to find provide word in a 2-d matrix of character.

        I solved this problem, however, 1 test case did not passed. I had no time to debug it. So, interviewer concluded the coding session there.
1. Last 5 min was left to conclude the interview. He just asked me if I have any question and told me to provide honest feedback.


I was happy with the interview. However, I did not had any hope about next steps as I read in the Internet that this stage is extremely hard and most of them did not passed even after acing the Interview.

My karat interview was at 3 PM on a Friday. I did not get any call for queit few days. In the mean time, I faced a health issue as I developed extreme back pain due my condition with PIVD and got sever allergies as side effect of pain killer. While I was suffering with this, I got email from interview co-ordinator regarding my next stage.


## Stag-2: Coding Interview

Next stag is coding interview. It is consisting two interviews, a) Code-Design interview and b) Data-Stucture and Algorithm interview. I schedule the interviews for two consecutive days. Each interview continues for 1 hour. For both the interviews, they asked me to keep my setup ready with prefered IDE with pefered tooling and Zoom.

### Stag-2.1: Coding Interview: Code-Design

Code-Design interview is a special interview where interviewer checks the code quality. It expect following things:
1. Code quality: Code should be
    * Easy to understand
    * Easy to extend
    * Easy to Test
2. Adaptability
    * Easy to adapt in changed requirement
3. Computer Science Concept
    * Exception
    * Test case
4. Rationality
    * All the decision while coding needs to be rational
5. Resourcefulness
    * Use of resources to get idea

After the initial introduction, the interviewer describe the problem. Initial the provided very few bits of the problem. I asked a ton of questions and he revealed more parts of the problem. He was expecting TDD. I never developed anything with TDD before. However, I started writing code, I understand how easy it is to get confident in the code, once I have the TDD.

The initial problem was as follows: Write a Cost Explorer. Basically a product have different packages and users want to know the cost for a year. The problem is extremely simple but TDD makes it time cosuming to develop. Anyway, once completed this task, interviewer extend it to provide estimation only to end-of-calendar year. I extended it. However, times was almost up. So, interviewer asked few follow up questions. The interview was good. I am satisfied as I have learned something.

### Stag-2.2: Coding Interview: Data-Structure and Algorithm
Next day I was for traditional Data-Structure and Algorithm coding round. Interviewer provided me the problem with minimal information. I asked several question and finally understand that the problem is about `finding closest parent of two or more nodes`. The problem itself is very easy, however it took time to write auxilary code and little time to debug. I finihsed it in time. He did not ask me any follow up questions. I am kind of disappointed with this interview.

Second interview was easy, however I think I may have asked too many questions which lead to dilute the problem which I solve.

Interview co-ordinator might call back next week.