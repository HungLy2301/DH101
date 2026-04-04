# Make 10: Games and Play

Katie and Hung

## The Artifact

<iframe src="week10-game.html" width="100%" height="900" style="border:1px solid #ccc; max-width:100%;"></iframe>

If the embed does not render in your current viewer, open the game directly here:

**[Play "The Interview" Game](week10-game.html)**

*The Interview* is an interactive narrative game built with Twine exploring the gap between authentic self and performed identity in the context of an AI job interview. The game presents the player with choices that appear meaningful but systematically reveal how much agency is illusory in evaluative systems.

The game consists of 9 passages with branching paths that converge toward two distinct endings, each offering a different perspective on the relationship between performance and authenticity. The writing uses procedural rhetoric through mechanics like timed pauses (measured in decimal seconds), percentile comparisons, and data retention language to make players feel the surveilling nature of the system itself.

The embedded game should be playable directly from this page when the site is served as a static website. If it still does not load here, use the direct link above.

## Design Statement

The Interview puts you in a waiting room you didn't choose to enter. You were submitted by an algorithm, selected by an algorithm, and now you're being evaluated by one. There is no small talk. There is a timer in the corner. The company is called HK Systems, and its AI interviewer, HK AI, has already begun recording your emotional tone before you've said a word.

The game is about the gap between who you are and who you're expected to perform being in a professional context. It becomes almost unbearable when the person on the other side of the desk isn't a person at all. Every question the AI asks is technically fair. "Describe yourself in three words." "Describe a time you failed." "If I told you this question didn't matter, would you still answer honestly?" These are real interview questions. What the game does is make visible how strange they actually are when you can't rely on human intuition to read between the lines.

The choices that matter most are the ones that seem small. Answering honestly ("Curious. Stubborn. Uncertain.") earns the response that your answer "deviates from the 94th percentile of successful candidates." Answering strategically ("Driven. Collaborative. Results-oriented.") earns "alignment noted." Neither response tells you whether you got the job. That's the point! The system acknowledges your input and processes it, and you're left holding the feeling without knowing what it means.

The AI's measured pauses (logged in decimal seconds) and the data retention revelation, that your hesitations will train the next version of this system, function as the game's procedural argument: you are not just being evaluated here, you are being used. The two endings lean into this differently. In Ending A, you said something true and that happened regardless of the outcome. In Ending B, you named the game, and the game continued anyway. Neither ending is a win. They're just two honest ways to leave a room that was never designed for you.

## Artist Statement

I came into this project thinking games were fundamentally about freedom. What I came out of it understanding is that games are actually about constraint, and what constraint reveals. The Interview doesn't give you freedom. It gives you choices that feel meaningful and then quietly reminds you that the system is processing them regardless of how you frame them. That's not a bug. That's the argument.

What surprised me most was how much the writing itself could act as a mechanic. I didn't need to code anything elaborate to make the player feel surveilled. I just needed the AI's responses to echo back numerical precision: "1.3 seconds," "94th percentile," "36 months." Those numbers do something to how you read everything that comes after them. The prose was the system. The system was the point.

AI collaboration was genuinely useful for structural thinking and for generating options I could react against. Where it fell short was in tone. Every time I tried to use Claude to draft a passage directly, the result was technically competent and emotionally flat in the way that "Driven. Collaborative. Results-oriented." is correct. I ended up using that flatness as a reference point: if my writing started sounding like an AI's suggestion, I knew I'd drifted from the voice I was going for.

If I did this again, I'd build in a third ending, where the player refuses to answer the final question at all, just lets the cursor blink. I think silence should be a playable choice. I ran out of time, but I know exactly what it would say: nothing, and that would be enough.

## Attribution & AI Use

### Tools Used

I used Claude (Anthropic) as my primary AI collaborator throughout this project.

### What I Asked AI to Help With

Early in the process, I had the core concept, an AI interviewer and a candidate who might resist. However, I wasn't sure how to shape the emotional arc. I asked Claude to help me think through how a player's feelings should shift from the start of the interview to the end. Claude suggested building around mounting discomfort rather than escalating drama, which matched what I was going for. I kept that framing and used it to decide which passages came first.

I used Claude to brainstorm questions that an AI interviewer might plausibly ask, ones that would feel corporate-normal on the surface but quietly uncomfortable underneath. It generated a range of options: productivity self-ratings, ideal manager descriptions, five-year plans. Most of these were too generic and I discarded them. The questions I ended up using were written by me, though Claude's list helped me understand what I was trying to avoid, which was its own kind of useful.

I asked Claude to look over the "Data Question" passage for pacing. During that conversation it suggested a phrasing variation that included the word "harvested" to describe how candidate data gets used. I liked the word and kept it, but rewrote the surrounding sentences entirely to fit the tone of the rest of the game.

I also asked Claude to explain Twine's Harlowe link syntax and how to handle passage branching that converges back to a single node. That was purely technical help with no bearing on the writing.

### What I Changed or Discarded

Claude's suggestions tended toward the explicit: it wanted to say things directly that I preferred to leave open. An early suggested line for the opening passage was something like: "The room feels like it was designed by an AI that had only read descriptions of waiting rooms." I thought it was too clever and too on-the-nose. I replaced it with my own version, which describes the white as the white of a loading screen, of a blank document. I wanted the strangeness to surface gradually rather than announce itself.

The two endings were entirely my own. I described the concept to Claude: one where the player accepts the human reality of the moment, one where they see the system clearly. I then asked whether the endings felt thematically earned. Claude said yes to Ending A and flagged that Ending B might feel deflating. I kept Ending B exactly as written. The deflation is the point.

### My Policy on AI Use

I use AI as a thinking partner and pressure-tester, not a ghostwriter. Every sentence that came from an AI suggestion was substantially rewritten before it entered the game. The voice in the passages is mine. AI helped me move faster and gave me things to push against, but it didn't write this game.
