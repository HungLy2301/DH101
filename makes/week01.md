# Week 1 – Reverse Engineering

## The Artifact
https://openai.com/dall-e
Prompt → model → image pipeline

## Process Notes
1. What Is Being Made?
DALL·E produces synthetic images based on text prompts provided by users. The output can be illustrations, paintings, posters, or realistic scenes that did not previously exist.
2. What Is the Project Made From? (Data)
The project is built from large scale image and text data used to train the model. These data include descriptions of images and visual patterns that help the system learn how words relate to visual elements. What is missing are the lived intentions, emotions, and personal meanings
behind images.
DALL·E's training data almost certainly reflects the biases of its sources: predominantly English-language captions, Western aesthetic conventions, and images that were already on the public web. What is excluded are images behind paywalls, images from communities that don't widely publish online, non-Western artistic traditions, and any visual knowledge that was never digitized. This has documented consequences: early image models consistently underrepresented darker skin tones, non-Western dress, and disability — not because of a single design decision, but because those images were statistically underrepresented in the training corpus. The pipeline from "internet images" to "trained model" launders those absences into outputs that feel neutral but aren't.
3. Tools, Algorithms, or Systems
DALL·E uses a text to image generation model that translates prompts into images. ChatGPT plays a guiding role by expanding and refining prompts for users. Much of the image generation process is automated, but guardrails and prompt interpretation are shaped by human design choices and policies.
4. Human Labor & Decisions
Humans collected and curated training data, designed the model architecture, and set safety limits. Human judgment determines what the system is allowed to generate and what is blocked. Even though the machine creates the final image, people shape the system's boundaries and creative direction.
5. Design as Argument
The interface makes image creation feel easy and playful, which hides the complexity and labor behind the system. It makes creativity feel accessible while making the underlying data sources and power structures harder to see.

## Reflection
In DALL·E, making is not a single act of drawing or designing, but a layered process involving prompts, models, data, and interface design. Making happens when users describe ideas, when ChatGPT reshapes those ideas into prompts, and when the model generates images based on learned patterns. When machines participate in making, creativity becomes shared between humans and systems. The machine can generate visuals quickly and at scale, but it does not understand meaning or intention the way humans do. Human values still shape what the machine can create, through training choices, safety rules, and interface design. As a result, making with AI shifts authorship and creativity into a collaborative but uneven relationship, where the machine produces outputs while humans define the limits, goals, and meanings behind them.
