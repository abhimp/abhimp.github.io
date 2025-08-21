---
layout: blog
title: Interview Experience - Stripe
menutype: blog
menu_order: 20
plink: interview_with_stripe_backend_engineer
---

# Stripe Interview

I am currently jobless and actively searching for a position. Recently, I received an email from [Stripe](https://stripe.com/). The recruiter asked me to schedule a telephonic discovery round.

I know about Stripe, and I also know that it is extremely difficult to crack, even more so than Atlassian. So, I am documenting everything here in case it's helpful for someone.

## Stage-1: Discovery Interview

The recruiter called me on time. At the very beginning, he told me the structure of the interview, which would start with a) his introduction, followed by b) my introduction, c) my interests and expertise, and d) a general discussion. From his introduction, I understood that he is a very accomplished and experienced recruiter. In fact, I don't think I have seen any other recruiter so accomplished. However, he was down-to-earth and very easy to have a conversation with. The interview went well. He told me what they were expecting. Among many things, he also asked me if I enjoy LeetCode because their interviews or coding rounds are nothing like it. During the discussion, he casually mentioned that almost no one from [VDX.TV](https://VDX.TV) had cracked their interviews. At the end, he asked me to schedule the first technical interview (they sent a Calendly link to schedule it).

## Stage-2: Coding Interview
I scheduled the interview for the next week so that I could have some time to prepare. However, I could not find much information on the internet. So, I stuck to generic preparation.

The interview started on time. The interviewer's profile was much better than mine, although he had less experience. He told me that the coding round would start with a simple problem which would be extended twice. He also told me that he didn't care about optimization; it was all about completion. Then we moved to the HackerRank platform for problem-solving. He asked me to choose a language, and I chose `Python 3`.

The first problem was to calculate the total cost of an order, where the order is a JSON object and they also provide a cost matrix. They were something like the following:

**Order**:

```js
{
    "country": "US", //it could be CA
    "order": [
        {"product": "laptop", "quantity": 5},
        {"product": "mouse", "quantity": 20}
    ]
}
```

**Cost Matrix**
```js
{
    "US": [
        {"product": "laptop", "cost": 1000},
        {"product": "mouse", "cost": 20}
    ],
    "CA": [
        {"product": "laptop", "cost": 1100},
        {"product": "mouse", "cost": 25}
    ]
}
```

The problem was pretty simple to solve. So, I did in approx 5min. While solving it, I asked various clarifying question. At the end, he asked me if I am missing any edge case or not. I told what every I could find at the time. So, we moved to next problem to a different tab. It already had the next problem. While I was reading the problem, he copied my last solution this current tab. They changed the cost matrix to include differential pricing based on quantity. It looks like following now:

**Cost Matrix**
```js
{
    "US": [
        {
            "product": "laptop",
            "costs": [
                {
                    "minQuantity": 0,
                    "maxQuantity": 2,
                    "cost": 1200
                },
                {
                    "minQuantity": 3,
                    "maxQuantity": 4,
                    "cost": 1100
                },
                {
                    "minQuantity": 5,
                    "maxQuantity": null,
                    "cost": 1000
                }
            ]
        },
        {
            "product": "mouse",
            "costs": [
                {
                    "minQuantity": 0,
                    "maxQuantity": null,
                    "cost": 20
                }
            ]
        }
    ],
    "CA": [
        {
            "product": "laptop",
            "costs": [
                {
                    "minQuantity": 0,
                    "maxQuantity": 2,
                    "cost": 1300
                },
                {
                    "minQuantity": 3,
                    "maxQuantity": 4,
                    "cost": 1200
                },
                {
                    "minQuantity": 5,
                    "maxQuantity": null,
                    "cost": 1100
                }
            ]
        },
        {
            "product": "mouse",
            "costs": [
                {
                    "minQuantity": 0,
                    "maxQuantity": null,
                    "cost": 25
                }
            ]
        }
    ]
}
```

The extended problem was pretty simple. However, there was little bug in my code which was causing both compilation error and inacurate result. It took me few minutes to figured it out by adding lots of print. When I finished this problem, it was 40min into the interview. So, after few quick questions on edge case, we moved to the next problem in the next tab. It was extended to add a `fixed` price in the matrix. So the cost matrix looks like following now.

**Cost Matrix**
```js
{
    "US": [
        {
            "product": "laptop",
            "costs": [
                {
                    "minQuantity": 0,
                    "maxQuantity": 2,
                    "cost": 1200,
                    "type": "fixed",
                },
                {
                    "minQuantity": 3,
                    "maxQuantity": 4,
                    "cost": 1100,
                    "type": "incremental"
                },
                {
                    "minQuantity": 5,
                    "maxQuantity": null,
                    "cost": 1000,
                    "type": "incremental"
                }
            ]
        },
        {
            "product": "mouse",
            "costs": [
                {
                    "minQuantity": 0,
                    "maxQuantity": null,
                    "cost": 20,
                    "type": "incremental"
                }
            ]
        }
    ],
    "CA": [
        {
            "product": "laptop",
            "costs": [
                {
                    "minQuantity": 0,
                    "maxQuantity": 2,
                    "cost": 1300,
                    "type": "fixed",
                },
                {
                    "minQuantity": 3,
                    "maxQuantity": 4,
                    "cost": 1200,
                    "type": "incremental"
                },
                {
                    "minQuantity": 5,
                    "maxQuantity": null,
                    "cost": 1100,
                    "type": "incremental"
                }
            ]
        },
        {
            "product": "mouse",
            "costs": [
                {
                    "minQuantity": 0,
                    "maxQuantity": null,
                    "cost": 25,
                    "type": "incremental"
                }
            ]
        }
    ]
}
```

It was so simple compared to last problem that it took only 2 line changes. My all three coding problem was completed with 45minutes into the the interview. As we had time, the interviewer said `lets stretch the problem little more`. He changed the problem little bit and asked me if my current solution would work or not. I understand little wrong, so I modified the code little bit (3 lines only). However, it wasn't required for his problem. I explained that and he was okay.

After we finished the coding round, we had around 10 minutes to kill. So, we discussed various stuff about stripe.

Now, wait begin for the result.