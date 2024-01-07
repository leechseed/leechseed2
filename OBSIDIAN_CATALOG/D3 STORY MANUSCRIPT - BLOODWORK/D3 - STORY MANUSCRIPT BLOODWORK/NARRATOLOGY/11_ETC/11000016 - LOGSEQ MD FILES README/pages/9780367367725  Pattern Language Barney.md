  public:: true
  
- # [Website](https://patternlanguageforgamedesign.com/)
- # **CONTENTS**
	- # SECTION I
	  collapsed:: true
		-
---
			- # 1 - What is this book for?
			  collapsed:: true
				- What is this book, then? It’s a book of exercises that will help you orga-
				  nize your understanding of design into a language that you can use to cre-  
				  ate games.  
				- This book does not provide a Pattern Language for game design. Instead,
				  it ofers a series of exercises for you to complete. Each one gives you a dif-  
				  ferent way to create a pattern. Once you’ve worked your way through this  
				  book, you can select the exercise that’s best suited for any design prob-  
				  lem you face, and complete it again to generate new patterns that ft your  
				  design needs.  
				- Over time, you’ll link all of the patterns you create to build
				  your own Pattern Language. Tis book contains only 24 exercises, but  
				  using them you can discover hundreds of patterns.  
				- This book encourages the development of a personal Pattern Language that is what you, as a developer, need.
				- The process of generating patterns through the exercises in this book forces you to think deeply about the mechanics and techniques used in the games you observe.
				- The exercises will help you understand the purpose behind those techniques, to see beyond their surface-level effects.
	- # SECTION II
	  collapsed:: true
		-
---
			- # 2 - Background on *A Pattern Language* by Christopher Alexander
			  collapsed:: true
				-
				  > Our world can be understood as if it were interwoven by conscious and unconscious patterns, whereby each pattern is linked to other patterns. (Leitner 2020)  
				-
				  > While pattern theory originates in architecture, it is a general theory of development (of change, of transformation, of unfolding, of the creative process) and, as such, is relevant to almost every feld of application, even for the very complex and for social systems. (Leitner 2015)  
				- All of this ties to the exercises in this book, which let you create a Pattern Language for games based on the patterns that you see. How you assess those patterns, which ones you see as “good” and which you see as “bad,” will be based on who you are, your experience playing games, your current design skills, and what you want players to get out of the games you design.
				- One of the most valid points raised against the work in A Pattern Language applies strongly to game design: the criticism that Alexander drew entirely from Western architectural tradition as a source for his patterns.
				- It is critical to understand the people that you are building for and to note as part of your patterns how tied to a specifc location or society they are.
				- In game terms, we must be aware of our audience both as we distill patterns and as we apply them.
			- # 3 - Background on the Use of Patern Languages in Other Fields
			  collapsed:: true
				- ## Computer Science
					-
					  > The real reason that common patterns are not used rather than tight abstractions is efficiency. It is more efficient to write abstracted, compressed code than uncompressed common patterns, and it is more efficient to execute abstracted code in some cases.  
					- Design Patterns: Elements of Reusable Object-Oriented Software (Gamma et al. 1994.) The authors of this book, often referred to as the “Gang of Four,” combined their considerable collective experience and looked at a presumably vast amount of object-oriented code to produce a set of well-defined, useful patterns.
					- The fundamental problem is that they are not design patterns; they are techniques that repeated across many designs.
					- They are useful in understanding how to structure aspects of that code in a functional way, but they lack the two qualities required to be patterns in the Alexandrian sense: they do not address specific design problems, and they do not have the structure of a language needed to produce whole designs.
				- ## Social and Behavioral Science
					- The most exciting outcome came from a group working on a Pattern Language for creative learning.
					- Their process consists of five steps: Pattern Mining, Pattern Prototyping, Pattern Writing, Language Organizing, and Catalogue Editing. The process is focused on providing a framework to generate a language needed by a subject area and produces a language document ready for publication.
					- The techniques you will learn in the following sections are focused on the process of creating a personal language. The language may find broad use, but its intended value is the understanding you gain by creating it.
			- # 4 - Background on the Use of Patterns in Game Design
			  collapsed:: true
				-
				  > Unlike most design patterns we have chosen not to define patterns as pure problem/solution pairs. Tis is due to two observations. First, defining patterns from problems creates a risk of viewing patterns as a method for only removing unwanted effects of a design. In other words, using patterns as a tool for problem-solving only and not as a tool to support creative design work. (Bjoörk et al. 2003)  
				- misunderstanding what Alexander meant by “problem.”
				-
				  > Each pattern describes a problem which occurs over and over again in our environment, and then describes the core of the solution to that problem, in such a way that you can use this solution a million times over, without ever doing it the same way twice. (Alexander 1977)  
				- The problem he was referring to was not a specific defect in a design that needed a solution, but the desired outcome of the design that needed a solution.
				- Design patterns allow you to build on that experience without going through a long learning period yourself.
				- to create assets that are in line with the theme, narrative design, and mechanical design, all disciplines must be engaging with the same design language.
				- For any Pattern Language to be complete enough to be useful, it must start at a high enough level to encompass each of those areas. Even for a design team divided into those areas, such a language would be necessary for those teams to best work together.
				- there is no statement of when or why creating a flow state is desirable. The implication that all games should produce this state is demonstrably false.
				- Te slow pace of a narrative game is not conducive to a fow state, and yet the games are immersive, compelling, and successful in their goals as games.
	- # SECTION III
	  collapsed:: true
		-
---
			- # 5 - An Introduction to Patterns in Game Design
			  collapsed:: true
				- ## The Pattern Template
					- This template represents a synthesis of the work of other designers in applying patterns to game design and my experience in using patterns to teach design.
					- ![image.png](../assets/image_1685719364565_0.png) ![image.png](../assets/image_1685719405537_0.png){:height 723, :width 540} ![image.png](../assets/image_1685719429087_0.png)
					-
					  > What is a design problem? The design problem that is addressed by a pattern should describe a situation you face as a designer. A design problem is not simply the effect of a mechanic stated as a question. It must capture the purpose and intent of the designer not just mechanically but in terms of its effect on the player. In this way, a well-constructed pattern will ensure that you are designing games that intentionally create an experience for the player. If this seems abstract, look over some of the design problems in the example patterns provided for each exercise.  
				- ## Pattern Confidence
					- All patterns start with a confidence rating of 0, then add 1 for each of the following items that apply.
					- Some of the items are related and “stack.” For example, a Common Pattern (+1) would also have to meet the requirements for being a Limited Pattern (+1) and a Singular Pattern (+1) for a total of 3. You should apply all the applicable labels. So if you had used this hypothetical pattern and another developer had independently described the same pattern, you would also apply Demonstrated Pattern” (+1) and Independent Sources (+1) for a total confidence score of 5.
					- **(+0) Theoretical Pattern**: The Theoretical Patterns exercise (Exercise 24) generates this type of pattern. You might also create a theoretical pattern by adapting a pattern from an existing repository that doesn’t cite example games. This pattern may be valid, but you don’t generate it from observation. Instead, you create it by imagining how a theory about game design would fit the pattern format.
					- **(+1) Single Example Pattern:** This level of confidence comes from a pattern that was generated based on one example. It’s entirely possible to look at a single game and derive a valid pattern from it. However, it can be challenging to determine whether what you see is an actual pattern or just the results of a design technique or element that would yield a different pattern if you looked at its use across many games.
					- **(+1) Limited Pattern**: If you’ve observed the pattern in fewer than ten games, it’s a limited pattern. If you have a hard time providing the ten examples in an exercise, this level of confidence may result.
					- **(+1) Common Pattern**: The pattern is visible in at least ten games, probably many more. You have found a “common pattern” when you stop recording examples at ten but could go on, and it’s a good sign that you’ve done an excellent job formulating a pattern based on your observations.
					- **(+1) Demonstrated Pattern**: A pattern is a demonstrated pattern if you, or another developer, have used it in development, and the effect was as intended.
					- **(+1) Validated Pattern**: This confidence level describes a pattern that’s in common use among a variety of game developers and has been proven effective through widespread use. At the time of the printing of this book, it’s probably not possible to find a pattern validated through use. As you work with patterns throughout your career, it may become more common. A pattern might also be a validated pattern if you conducted empirical user
					  research to show that the pattern was effective.  
					- (+1) Independent Sources: If more than one developer derives a pat-tern, it has independent sources. In teaching, it’s common to discover this kind of pattern as more than one group of students arrives at the same pat-tern from different starting points. As the community of developers using the exercises in this book increases and shares patterns, this will become more common.
				- ## Example Pattern
					- ![image.png](../assets/image_1685719986575_0.png) ![image.png](../assets/image_1685720005608_0.png) ![image.png](../assets/image_1685720020114_0.png)
					- Initially, when you are creating a pattern, you leave the last three items blank. You may not be able to identify parent and child relationships when you first complete the pattern, because you will have such a small set of patterns. As you develop more patterns, you will add these fields when you recognize that two of your patterns are connected.
				- ## Introduction to Pattern Exercises
					- As you work through this book, I encourage you to do the exercises in order. They build in complexity and specificity, and passing through all of them once will give you the start of a structure for the language you will develop from them
					- Once you have completed the exercises once to build the foundation of your language, you will be comfortable with the process.
					- ^^Each pattern exercise in this book consists of a set of steps.^^ They begin with a framing task/question: **name a functional design element**, or **pick a mechanic from a boss encounter**, or **choose an emotional effect**.
					- You are then usually asked to list, through research or experience, a set of games that match the design element you’ve chosen.
					- You then analyze those games and how they achieve the effect you observed in them.
					- You need to describe what you see in some detail, again avoiding using only one or two keywords.
					- It’s surprising what insights you can get when you force yourself to describe precisely the thing that seems evident to you.
					- Next, you will look at the games you’ve analyzed and see if you observe any patterns. The exercises ask you to find ten games. Tat number is arbitrary; it is both too large for many new designers and far too small to generate indisputable patterns.
					- However, listing ten games will force you to look at edge cases and pick at least a few games that were not immediately obvious to you. These games will help you understand the scope of your pattern.
					- Tese exercises help you fnd and defne potential patterns. Don’t think that because you were able to complete an exercise that the pattern you have observed is true in some fundamental way
					- ![image.png](../assets/image_1685720361278_0.png)
					- ### Step 1: Name a Design Element
						- A tall structure, visible from many points in the game world.
						- `The first step, name a design element, is intentionally vague. It will allow you to apply this exercise to virtually any design problem. However, it doesn’t give much guidance for you to focus the pattern in any particular way. Tat makes this a good exercise for creating general, broadly applicable patterns.`
					- ### Step 2: What problem(s) does that design element solve?
						- A. Architectural weenies help motivate and facilitate the player’s exploration of the world. These are two related but distinct functions. I suspect that there are child patterns* related to each.
						  B. Architectural weenies may create an iconic image or location to set the tone of the game, such as the Great Tree in Ori and the Blind Forest or the glowing mountain in Journey.  
						  C. They can also create a narrative focus for the game, e.g., Death Mountain in many Zelda games or the White-Gold Tower in the Imperial City in The Elder Scrolls: Oblivion.  
						- `The next question, What problem(s) does that design element solve?, is intended to get the designer to start thinking about what purposes design elements serve. It’s crucial to think carefully and identify actual design problems, rather than just restating the mechanic. For instance, if the design element were “jumping,” it would not exist to solve the problem of “letting the player jump.” Instead, perhaps “allowing dynamic traversal” or, better yet, “increasing player autonomy by creating more dynamic movement options.”`
					- ### Step 3: Pick one of the problems you Identified
						- A. Motivating and facilitating the player’s exploration of the world.
						- `In this case, I identified three effects that might be created by an architectural weenie. I chose the first one to explore in the rest of the exercise.`
						- `The next step asks you to name at least ten games that solve the same problem as the design element you chose rather than ten games that use that same design element.`
						- `Exercise 1: Basic Pattern Exercise looks at the design element directly`
						- `Exercise 2: Higher-Order Patterns looks at the problems solved by the design element.`
						- `Focusing on the problems allows the exercise to uncover more fundamental patterns by looking at the underlying purpose of the design element rather than the element itself. The phrase “higher order” here is about zooming out just a little, going from narrower to broader, from specific to more general.`
					- ### Step 4: List and describe ten games that also solve the same problem in as many diverse ways as possible
						- Journey, Grand Theft Auto, Assassins Creed, Skyrim, Bastion, Dear
						  Esther, The Secret World, Draugen, Anthem, The Room  
						- `Question 4 is relatively simple, but probably requires the most time to complete. In this case, how do Journey, Grand Theft Auto, etc. motivate player exploration.`
						- `If you don’t, you may end up converging back to a pattern that just describes the technique you began with.`
						- `The goal of this exercise, in terms of the example, is not to describe architectural weenies but to understand the higher-level, more fundamental pattern that they express.`
					- ### Step 5: Describe the way each game solves the design problem. Focus on each game and try *not* to start looking for patterns as you write
						- *Journey*—The mountain in the distance in Journey gives you a
						  sense of direction and has a visually compelling, unexplained  
						  light shining from its top.  
						- *Journey*—The ruins that you can see in the near distance
						  throughout the game stand out from the initial desert land-  
						  scape, offering direction; when you get close, you can see the  
						  embedded narrative of the partial murals on the ruin walls.  
						- *Grand Theft Auto*—There’s a map showing where it’s possible
						  to go, but the map is incomplete, which gives you a limited set  
						  of short-term goals and teases future quests with the negative  
						  space on the map.  
						- *Assassin’s Creed*—The landscape you move through as you
						  play contains many high towers. Given the game’s climbing  
						  mechanics, they are attractive locations. The quest map is filled  
						  in by showing more and more possible quest objectives with  
						  each tower you reach.  
						- *Skyrim* (and many Elder Scrolls games)—The Icons that appear on
						  the compass indicating points of interest provide immediate directions for exploration. They show you what kind of quest you will  
						  encounter by going in a direction, but don’t give you any details.  
						- *Bastion*—The world around the character is very limited but
						  forms continuously as you move so that every action results in  
						  more of the world’s secrets revealing themselves.  
						- *Dear Esther*—There’s no apparent direction or goal at the
						  beginning of the game, but you have only a few paths you can  
						  follow. As you move, you hear and see narrative snippets that  
						  raise more questions than they answer.  
						- *The Secret World*—One activity you can do in this massively
						  multiplayer online game (MMO) is collecting “Lore” snippets,  
						  which appear as visually distinct hovering items in the game  
						  world. Each one contains a bit of a story, but you usually fnd  
						  them out of order.  
						- *Draugen*—The world constantly presents appealing but inaccessible exploration options; most become available as the
						  game progresses.  
						- *Anthem*—Much of the drive to explore comes from enticing vistas and collectible narrative items. But you also need
						  resources, and exploring is the best way to get them in the early  
						  part of the game.  
						- *The Room*—Tis mobile game presents you with one strange
						  puzzle box after another, and you’re always given just enough  
						  information to open it, but rarely any information about what  
						  you’ll find when you do. The game narratively implies occult  
						  mysteries at every opportunity.  
						- `The next question is probably the hardest. Here I ask for you to look for patterns. It is entirely possible, though unlikely, that no patterns exist for you to find. It's also possible that several or even many patterns may be present. In this case, I just list a single aspect that example games share.`
						-
					- ### Step 6: What do those solutions have in common? The solutions may have more than one thing in common. Some games may share one, and other games share another. List and describe each.
						- They all provide the player with partial information.
						- `If I had listen more than one property that the games had in common, I would have listed each here and considered whether each was related to the others.`
						- `Finally, I ask you to articulate the pattern that you've observed. The response usually comes in the form of a short paragraph. In the next step you fill out the Pattern Template using the answers you gave all in the preceding steps.`
					- ### Step 7: Is there a pattern? Briefly describe it. Do not create a formal description using the Pattern Template; just make the first attempt to articulate what you see.
						- `It’s important to note that the Example Games section of the
						  Pattern Template is not asking for the games from question 4 of the  
						  Pattern Exercise, which asked for ten games that solved the design  
						  problem in different ways. It’s asking for ten games that implement  
						  the pattern as you have identified it in question 7 of the exercise  
						  where you articulated the pattern. These may or may not be the same  
						  games, and, in fact, easily finding additional games that implement  
						  the pattern is a sign that the pattern is a good one.`  
						- `It's important to note that the Example Games section of the Pattern Template is not asking for the games from question 4 of the Pattern Exercise, which asked for ten games that solved the design problem in different ways.`
						- `It's asking for ten games that implement the pattern as you ahve identified it in question 7 of the exercise where you articulated the pattern.`
						- `These may or may not be the same games, and, in fact, easily finding additional games that implement the pattern is a sign that the patter is a good one.`
					- ### Step 8: For each problem you identified in step 2, you may repeat steps 3-7
						- `If I wished, I could have returned to step 2 and looked for patterns related to the other two design problems that I listed there.`
				-
			- # 6 - Principles of Good Pattern Design
				- ## 1 Patterns Should Address a Design Problem
					- *“In order to y, designers may wish to x.”*
				- ## 2 Avoid Shallow Patterns
					- It’s not enough to just look at what a game does.
					- When analyzing a game, that’s an example of your pattern; it’s essential to look at why it’s doing what you say it’s doing.
				- ## 3  Do Not Create Circular Patterns
					- Check to see if your pattern is in the format:
					- *“To do x you should create a game that does x.”*
					- If it is, your pattern is circular.
				- ## 4  Patterns Should Be Prescriptive
					- *To create situations where players can explore the identities of their characters in an RPG, designers may create situations where the character’s actions will have important but easily identified and contained effects on the game world.*
				- ## 5 Avoid Jumping to Conclusions
				- ## 6 Anti-Patterns are not Bad Patterns
				- This section is fucking frustrating and retarded and reads like a shitty blog post. fuck this asshole
-
- # Reference
- # Types of Patterns
  collapsed:: true
	- ## Basic
	- ## Higher-Order
	- ## Lower-Order
	- ## Formal
	- ## Functional
	- ## Emotional
	- ## Player Experience
	- ## Theme
	-
---
	- ## Basic Pattern
	  collapsed:: true
		- Purpose: Broadly applicable and can be used to generate new pattern types
		- ![image.png](../assets/image_1686915985812_0.png)
	- ## Higher-Order Pattern
	  collapsed:: true
		- Purpose: A broad-ranging pattern that is comprised of more detailed or complimentary patterns.
		- Systemic
		- ![image.png](../assets/image_1686915964843_0.png)
	- ## Lower-Order Pattern
	  collapsed:: true
		- Purpose: Pattern that is dependent on a higher-order pattern
		- ![image.png](../assets/image_1686915938797_0.png)
		- ![image.png](../assets/image_1686915945178_0.png)
	- ## Formal Pattern
	  collapsed:: true
		- Patterns that are considered the structural forms of the game. Dude this guy is so fucking retarded. Higher order? Formal? like dude doens't describe shit.
		- Focuses on Systemic patterns that **centered around the world that the player exists in**
		- ![image.png](../assets/image_1686915926627_0.png)
	- ## Functional Pattern
	  collapsed:: true
		- Purpose: Patterns that require interaction of a user, consider *-ing* verbs
		- ![image.png](../assets/image_1686915904228_0.png)
		- ![image.png](../assets/image_1686915911859_0.png)
	- ## Emotional Pattern
	  collapsed:: true
		- Purpose: Emotional effects that are incited by the game using interaction unique to video games.
		- ![image.png](../assets/image_1686915887283_0.png)
	- ## Player Experience Pattern
	  collapsed:: true
		- Purpose: Patterns that shape player experience
		- ![image.png](../assets/image_1686916051299_0.png)
	- ## Theme Genre Pattern
	  collapsed:: true
		- Purpose: Aesthetic Genre
		- ![image.png](../assets/image_1686916099818_0.png)
	- ## Circulation Patterns
	  collapsed:: true
		- Purpose: To Identify **Gameplay Loops** that players act upon in a macro, micro, and meta sense.
		- ![image.png](../assets/image_1686916237846_0.png)
	- ## Boss Encounter Patterns
	  collapsed:: true
		- Purpose: Focuses on Boss Encounters
		- ![image.png](../assets/image_1686916279765_0.png)
	- ## Emergent Narrative Patterns
	  collapsed:: true
		- Purpose: Story beats that are created by player interaction with game systems, then joined into a coherent narrative in the player's mind.
		- ![image.png](../assets/image_1686916326887_0.png)
	- ## Embedded and Environmental Narrative Patterns
	  collapsed:: true
		- Purpose: This fucking retard says they're the same but different. They're different but they use the same pattern HUH? fucking idiot
		- **Environmental Narrative Patterns**
			- Purpose: Environmental elements and assets assembled in the game world when observed by the player create a meta-narrative within the space that the player exists. It is not required for the user to interact with these environmental narrative patterns to fulfil requirements of the story.
		- **Embedded Narrative Patterns**
			- Purpose: Diegetic elements that are placed within the game world with specific intent to forward the narrative of the game. The user must interact with an embedded narrative pattern to fulfill the requirements of the story, unlike the environmental narrative patterns.
		- ![image.png](../assets/image_1686916621047_0.png)
	- ## Breaking Spaces Patterns
		- Purpose: Locus of Play - understanding the meta-cognitive/physical spaces in which users play the game, and how games shift from one medium to another. Highly related to the intertextual hypermediated nature of videogames such as *Fortnight*
		- ![image.png](../assets/image_1686916754914_0.png)
		- ![image.png](../assets/image_1686916763912_0.png)
	- ## Player Manipulation Patterns
		- Pattern Purpose: Since we’re trying to create a player experience with the games we design, the behavior of players in response to our games is a critical component.
		- ![image.png](../assets/image_1686987157026_0.png)
	- ## Patterns in Innovation
		- Pattern Purpose: This exercise looks at the ways that games are innovative and uncovers the patterns they use to create that innovation.
		- ![image.png](../assets/image_1686987242000_0.png)
		- ![image.png](../assets/image_1686987248468_0.png)
- # Christopher Alexander's  *Lebendigkeit* or the Nature of Order
  collapsed:: true
	- levels of scale
	- strong centers
	- boundaries
	- alternating repetition
	- positive space
	- good shape
	- local symmetries
	- deep interlock
	- contrast
	- graded variation
	- roughness
	- echoes
	- the void
	- inner calm
	- not separateness
	-
---
	- ### **Levels of Scale**:
	- This property refers to the balance and coherence among different scales in the design. For example, the various parts of a design should have a coherent and harmonious relation of scale with one another.
		- ![image.png](../assets/image_1686985881072_0.png)
		- *FIGURE 13.1 Not just ships, but the flying mechanic existing at three levels of scale. *
	-
---
	- ### **Strong Centers**:
	- These are areas or points in a design that draw attention and serve as the main focus of the design. They provide a sense of unity and coherence.
		- ![image.png](../assets/image_1686985932695_0.png)
		- *FIGURE 13.2 Each system is complete in itself and also contributes to the overall game. *
	-
---
	- ### **Boundaries**:
	- Boundaries help to separate and define areas of a design, thereby strengthening centers. They may be physical separations or marked by a change in pattern or color.
		- ![image.png](../assets/image_1686985960043_0.png)
		- *FIGURE 13.3 Not just clear literal boundaries in gamespace, but boundaries between game systems. *
	-
---
	- ### **Alternating Repetition**:
	- This property refers to the rhythmic repetition of elements in a design, providing a sense of unity and variety at the same time. The repetition is often in an alternating pattern.
		- ![image.png](../assets/image_1686985974441_0.png)
		- *FIGURE 13.4 Alternating repetition in the flow of gameplay. *
	-
---
	- ### **Positive Space**:
	- In Alexander's view, positive space is a continuous and coherent space shaped and filled by buildings, or other design elements, rather than leftover space that occurs after the buildings are placed.
		- ![image.png](../assets/image_1686986013776_0.png)
		- *FIGURE 13.5 All the elements the game needs and only the elements that are needed. *
	-
---
	- ### **Good Shape**:
		- This refers to the use of shapes that are inherently pleasing and balanced. These shapes are simple, coherent, and have clear boundaries.
		- ![image.png](../assets/image_1686986035865_0.png)
		- *FIGURE 13.6 Each “shape” in the game is pleasing and fits the whole, whether it is a space, a mechanic, or a piece of the story. *
	-
---
	- ### **Local Symmetries**:
	- Although global symmetry can be rigid, local symmetries refer to smaller symmetrical arrangements within the larger non-symmetrical context, providing a sense of order and harmony.
		- ![image.png](../assets/image_1686986061304_0.png)
		- *FIGURE 13.7 Two asymmetrical armies in asymmetrical siege warfare, but with symmetry between some units. *
	-
---
	- ### **Deep Interlock**:
	- This property refers to the way that components in a design interconnect and interrelate, often in complex ways, with one another. It can also mean that the elements of a design are so well integrated with each other that they interlock.
		- ![image.png](../assets/image_1686986073208_0.png)
		- *FIGURE 13.8 The deep interlock of the traditional holy trinity of classes in mas-sively multiplayer online games. *
	-
---
	- ### **Contrast**:
	- This property refers to the use of contrasting elements to create interest and tension within the design.
		- ![image.png](../assets/image_1686986084889_0.png)
		- *FIGURE 13.9 The contrasting game spaces of open fields and a maze. *
	-
---
	- ### **Graded Variation**:
	- Refers to the gradual or progressive variation in the design, such as changes in size, color, or form, rather than abrupt or random variation.
		- ![image.png](../assets/image_1686986354345_0.png)
		- *FIGURE 13.10 The gradual shift from the darkness of a dungeon to the light of day. *
	-
---
	- ### **Roughness**:
	- This property suggests that designs should embrace natural imperfection and asymmetry, acknowledging that real-world conditions often lead to deviations from idealized geometric precision.
		- ![image.png](../assets/image_1686986393499_0.png)
		- *FIGURE 13.11 Roughness in input mechanics as well as in textures or plot. (above)*
		-
		- ![image.png](../assets/image_1686986441530_0.png){:height 487, :width 445}
		- *FIGURE 13.12 A distressed texture might be the most literal example of rough-ness in a game. *
	-
---
	- ### **Echoes**:
	- This property suggests the subtle repetition of certain motifs or patterns throughout the design, creating a sense of unity and coherence.
		- ![image.png](../assets/image_1686986452130_0.png)
		- *FIGURE 13.13 Echoes occurring in spaces but also in mechanics and narrative. *
	-
---
	- ### **The Void**:
	- In Alexander's design philosophy, the void is a quiet, still, empty place at the heart of a design. It serves as a counterpoint to busier, more complex elements.
		- ![image.png](../assets/image_1686986467398_0.png){:height 455, :width 625}
		- *FIGURE 13.14 Sometimes the experience of space and gameplay is defined by the things that are absent from it. 
		  *  
	-
---
	- ### **Inner Calm**:
	- This property refers to the creation of a sense of tranquility or calmness within a design, often achieved through simplicity and order.
		- ![image.png](../assets/image_1686986477083_0.png)
		- *FIGURE 13.15 Fighting the constant drive to add features to meet genre and audience expectations.*
	-
---
	- ### **Not Separateness**:
	- This final property implies that the design should not feel separate or disjointed from its surroundings. It should instead harmoniously fit into its environment, echoing and complementing the characteristics of the site.
		- ![image.png](../assets/image_1686986497173_0.png)
		- *FIGURE 13.16 Each part of the game connected meaningfully to the next.*
	-
---
- # Advanced Pattern-Generation
  collapsed:: true
	- ## Patterns from Core Mechanics
		- Purpose: Understanding how sets of mechanics combine to create singular user experiences is essential. This exercise will help you to see and articulate these combinations of mechanics, and produce the patterns that govern how to create groupings like this effectively.
		- ![image.png](../assets/image_1686987476891_0.png)
		- ![image.png](../assets/image_1686987486316_0.png)
	- ## Finding Missing Patterns
		- Purpose: This exercise looks at an existing pattern and asks whether it’s effective in isolation. The answer to this question is almost always no, or if it is yes, then it could solve the problem more effectively if it was supported by parent and child patterns that reinforced its effect.
		- ![image.png](../assets/image_1686987778469_0.png)
	- ## Finding Negative Patterns
		- Purpose:  These patterns have some utility in terms of avoiding bad design. But they’re also useful as a way to understand a given problem. Mapping out negative patterns around a problem can make it clearer where to look for the patterns that solve it.
		- ![image.png](../assets/image_1686987821910_0.png)
	- ## Finding Positive Patterns from Negative Ones
		- Purpose: This exercise is intended to help you observe any possible patterns that are the obverse of negative patterns found using the previous exercise. In plain English, this exercise will help you check to see if reversing a negative pat-tern is likely to reverse the effect of that pattern.
		- ![image.png](../assets/image_1686987879615_0.png)
	- ## Using Patterns for Understanding
		- Purpose: Tis exercise looks at the effects of a technique. It might be formal or functional; it might be from any game design discipline. When looking at a technique in previous exercises, you may have noted that a technique has several different effects under different conditions.
		- ![image.png](../assets/image_1686987932592_0.png)
	- ## Understanding Tropes
		- Purpose: This exercise can help a developer assess the effects of a trope on their game. It’s not an exercise intended to convert a trope into a pattern.
		- ![image.png](../assets/image_1686987969105_0.png)
	- ## The First Choice
		- Purpose: This exercise is meant to produce very high-level patterns. It asks the designer to pick the first question they ask themselves when they’re asked to make a game.
		- ![image.png](../assets/image_1686988021895_0.png)
	- ## Audience Patterns
		- Purpose: Games have different effects on different players. It’s more useful to examine the effects of games on different people and observe patterns.
		- ![image.png](../assets/image_1686988078592_0.png)
	- ## Theoretical Patterns
		- Purpose: This exercise will allow you to propose a pattern without examples, a pattern that you think should exist based on a theory in game design.
		- ![image.png](../assets/image_1686988193857_0.png)
- # Core Steps in Creating a Pattern Exercise
  collapsed:: true
	- Pattern exercises usually consist of five to ten steps that guide the developer through the process of creating the pattern. These steps break down into four sections:
	- ![image.png](../assets/image_1686988652664_0.png)
-
---
- # Full Pattern Walkthrough  - Exercise 16
  collapsed:: true
	- ![image.png](../assets/image_1686987476891_0.png)
	- ![image.png](../assets/image_1686987486316_0.png)
-
---
- # Example: Pattern from Core Mechanics
  collapsed:: true
	- ## Step 1: Pick a game.
		- Anthem
	- ## Step 2: Write down how a non-designer would describe what makes that game awesome.
		- You have an Ironman suit and you can fly anywhere in this whole crazy world and blow things up with your friends!
	- ## Step 3: Figure out what they’re actually describing.
		- High levels of player mobility.
		- Wide choice of activities or objectives.
		- Cooperative asymmetrical combat.
		- Level/world design that takes advantage of player movement abilities.
		- Beautiful space to explore.
		-
		  > ` So, which of these mechanics are core? I would say that high levels of player mobility and the choice of activity or objectives are the core mechanics. Multiplayer supports the fun of the core mechanics. Good level and world design make the core mechanics challenging and rewarding. And the beautiful world helps drive the exploration. This is a complex game, and there are many patterns that work to support the core mechanics, including a loot-based progression system and a mysterious setting. Still, the strongest center is the ability to go anywhere and do anything.`  
	- ## Step 4: Describe the consequences of the mechanic you described in step 3. How does the mechanic you identified create the experience the player described?
		- From the very beginning of the game, the player has almost unparalleled mobility. The ability to fly and travel at speed through a large world creates a sense of freedom and empowerment. The game drives exploration through assigned plot missions early in the game, but play is intended to extend beyond the completion of the plot. Motivation is extended somewhat by the inclusion of collectibles and lots of long-term objective-completion goals. However, these alone would be insufficient to maintain long-term interest in the game. Character power progression and challenges of escalating difficulty are the primary drivers of play at this point. The activities that players continue to engage in are the ones that allow them to make meaningful progress on this axis.
		- Where the game fails is in the places where activities that are intrinsically enjoyable become meaningless on the axis of character progression.* So, world exploration and engaging in emergent play lose focus, even though they are intrinsically enjoyable elements. Completing linear, instanced scenarios gains focus, and while it’s an enjoyable aspect of play for many players, it deviates from the core gameplay loop of exploration and discovering unexpected challenges and events.
	- ## Step 5: Name and describe the way that ten other games use that mechanic to create the same experience.
		- *Assassin’s Creed: Black Flag—* This franchise in general uses free movement and diverse goals in an open world as its core gameplay loop. This general design choice is bolstered by the addition of an island-based map that lets you sail to any island at almost any time. The overall progress of this single-player game is more limited, so there is less of an issue of motivating long-term play. Moving through the game world freely, in this case by climbing or sailing, is similarly gratifying. This core mechanic is hindered by the fact that many of the activities that you can pursue—collectibles in particular—feel artificial, and are neither intrinsically fun or extrinsically rewarded by progression systems. As a result, they don’t drive the core game-play loop effectively.
		- *The Elder Scrolls—* This game may only partially fit this mold, in that the nature of the physical movement through the game world is not a focus of the game. It does fit in the sense that it’s an open-world game, and provides a wide variety of activities to engage in during play. The mechanics of player progression are tied to every activity you can perform, and so whatever activity you pur-sue, your character advances in power. If there’s a weakness in the implementation of these core mechanics, it’s that the activities you can engage in don’t always tie strongly into an overarching narrative.
		- *Ori and the Blind Forest*—In contrast to the preceding game, movement is the primary focus of this game. Your ability to explore the world is limited by the skills and movement abilities you have access to. In this way, this game doesn’t fit the pattern, in that exploration is gated by movement. However, the very limiting of movement allows the game to maintain a relatively constant level of difficulty, even as the abilities available to the character grow. The further you progress in the game, the more open the world becomes, and the closer it gets to the core mechanic of Anthem.
		- *Minecraft*—As with the graphical presentation, movement in this game is primitive. But because of your ability to alter the world, you’re able to move freely throughout the world. The developers haven’t done much to structure player behavior in this game in terms of setting specific goals. But the crafting progression and resource distribution systems make the game’s player movement abilities—that is, world-altering abilities—a perfect embodiment of the “go anywhere, do anything” core mechanic.
		- *Eve Online*—In this massively multiplayer game, which simulates vast sprawling space empires struggling for profit and dominance, the individual players have free movement in a local sense. You can move anywhere in the larger conceptual space of the universe, though that’s mitigated by the danger posed by other players and enemies present in those locations. The game is overall very skill-based, and it takes a long time to acquire many of those skills. However, since the game has existed for well over a decade, a large percentage of players are able to engage in virtually any activity that’s possible within the game. While player progression is a major driver of player activity for the game’s long, leveling-up period, the core gameplay is also driven by the complex oppositional activities of other players. Which is to say, you can go anywhere and do anything, but many of the things you might do either oppose the activities of other players or will be opposed by them. This creates sustainable long-term play for players that find the available activities compelling.
		- *Horizon Zero Dawn*—While the spatial movement in this game is more dynamic than in a game like Skyrim, it's not as free as in a game like Anthem or Assassin’s Creed. Character abilities like climbing and rappelling are limited to areas designated by the developers. There’s a strong linear story progression that gates access to the different areas of the map, but once areas become accessible, they are freely explorable. As in the Assassin’s Creed games, there are collectible systems present in the game, though here there’s at least some narrative and mechanical justification for them. The emergent challenge of fighting the large-scale monsters in this game provides per-haps the most intrinsically compelling “do anything” gameplay out of these example games.
		- *Dungeons & Dragons*—As a tabletop role-playing game with a human game master, this game truly allows players to go anywhere and do anything. Complex and fine-grained character progression provides long-term mechanical motivation for player exploration and activities. The game master provides narrative motivation, so the degree to which it’s compelling is tied to the game master’s storytelling ability.
		- *Pokémon Go*—In this geolocated augmented reality game, the character’s ability to go anywhere is limited by where the player can physically go. At release, the options available for player interaction were very limited, allowing only for capturing new Pokémon and collecting resources at geolocated points. In the three-plus years since the game’s release, the diversity of gameplay available has increased dramatically and is comparable to that available in the console versions of the franchise.
	- ## Step 6: List any patterns you see.
		- 1. The degree to which dynamic spatial movement (flying and climbing in most cases) is compelling is tied to how meaningful the character/player reasons are for going to places accessible through that movement.
		- 2. How compelling optional (or required) player activities are is deter-mined by a number of factors including:
			- a.	Narrative relevance
			- b. Intrinsic activity fun
			- c.	Contribution to character progression
		- 3. The greater the degree of character freedom (of movement or choice), the stronger the motivation required to make players feel like the choices they make are enjoyable and rewarding.
		- 4. As player movement options increase, players have more choices of where they can go at any given moment. When combined with many activity options in open-world games, this freedom can create decision paralysis and flat-seeming gameplay.
	- ## Step 7: Choose one pattern and document it using the Pattern Template.
		- 3. Greater choice requires greater motivation.
	- ## Step 8: You may repeat step 7 for each pattern you observed.
- # Final Result
  collapsed:: true
	- **Name:** Greater Choice Requires Greater Motivation
	- **Conﬁdence:** 2
	- **Image:**
		- ![image.png](../assets/image_1686991598279_0.png)
			- *FIGURE 14.1 Too many quests can be overwhelming, but seeing a burning building makes the choice clear.*
	- **Author:** Chris Barney
	- **Design problem:** How do you keep players motivated to explore and interact with systems as the scale of the game world and available activities increase?
	- **Description:** The greater the degree of character freedom (of movement or choice), the stronger the motivation required to make players feel like the choices they make are enjoyable and rewarding. n a very linear game, every player action visibly leads to progress, and the player is unlikely to feel that their actions aren’t meaningful. When games are nonlinear, allow a lot of player exploration, or give constant action options, players might not be sure which actions are optimal, i.e., whether they’re generating meaningful progress or are just a waste of time. Players thus require more and more motivation to feel conﬁdent in their choice to pursue a particular action. There are many patterns that suggest how to generate player motivation; they tend to indicate that any possible activities in the game should provide either meaningful narrative or mechanical progress, and ensure the player understands the nature of that progress.
	- **Games that use this pattern and how: **
		- *Horizon Zero Dawn*—While the spatial movement in this game is more dynamic than in a game like Skyrim, it's not as free as in a game like Anthem or Assassin’s Creed. Character abilities like climbing and rappelling are limited to areas designated by the developers. There’s a strong linear story progression that gates access to the different areas of the map, but once areas become accessible, they are freely explorable. As in the Assassin’s Creed games, there are collectible systems present in the game, though here there’s at least some narrative and mechanical justification for them. The emergent challenge of fighting the large-scale monsters in this game provides per-haps the most intrinsically compelling “do anything” gameplay out of these example games.
		- *Ori and the Blind Forest*—In contrast to the preceding game, movement is the primary focus of this game. Your ability to explore the world is limited by the skills and movement abilities you have access to. In this way, this game doesn’t fit the pattern, in that exploration is gated by movement. However, the very limiting of movement allows the game to maintain a relatively constant level of difficulty, even as the abilities available to the character grow. The further you progress in the game, the more open the world becomes, and the closer it gets to the core mechanic of Anthem.
		- The game is essentially over once the world is completely open, so in that sense, this game might be seen as falling outside of this pattern. However, there’s motivation to return to previously visited spaces to collect resources you need to continue character progression. This progression, of course, unlocks further movement options, and the cycle repeats. In terms of story, a strong overarching narrative motivates the player, but short-term motivation is generally very simple and disconnected from the larger meaning of the game.
		- Pokémon Go—As a geolocated augmented reality game, Pokémon Go limits the character’s ability to go anywhere using the player’s ability to move through non-digital space. It’s likely that no other game has as large and dense a playspace, with the exceptions of Niantic’s other games that use the same dataset of interaction locations. As a player in this game, you can literally go anywhere. In keeping with this pattern, each activity the player may engage in must provide the player with a strong sense of motivation. The game achieves this through the deep interlock of all its systems. Each system provides the resources for inter-acting with the other systems, and every system is resourced by multiple other systems. This allows players to engage only with activities they also ﬁnd intrinsically rewarding.
		- **Seed:** Exercise 16: Patterns from Core Mechanics—Go anywhere, do anything
		- **Related patterns:**
		- **Parent patterns:**
		- The Three Pillars of Meaning* (Conﬁdence: 2)—When trying to apply Greater Choice Requires Greater Motivation, this pattern describes the way that motivation can combine with context and consequence to create meaning. (At least in the context of emergent narrative as described in this pattern.)
		-
---
		- SUGGESTED EXERCISE
		- Use Exercise 9: Circulation Patterns to generate a pattern about cir-culation systems for exploration in open world games.
		- **Child patterns:**
		- Mystery-Driven Exploration† (Conﬁdence: 2)—Navigation and exploration are one set of choices that Greater Choice Requires Greater Motivation can help players to make. The more options for exploration a player faces, the more compelling a mystery will need to be to drive the player.
		- **Keywords:** Autonomy, Choice, Meaning, Motivation, Open World, Deep Interlock, Inner Calm
-
---
- # Each Design Pattern Exercise from Barney
- ### *First Editing pass. Enabling each design pattern exercise to be applied across media*
	- ## EXERCISE 1: BASIC PATTERN EXERCISE
		- Step 1: Identify a form in chaos.
		- Justify identification thru observation, notation, and design theory.
		-
		- Step 2: Identify 10 media that use that design
		- Step 3: Observe how each media uses design Focus on accurately describing the way each craftwerk uses the element you identified.
		- Step 4: What design problems do the craftwerks use the element to solve? Some craftwerks may use the element for one purpose, while others use it for another. Many craftwerks use the elements in more than one way. Describe the problems solved by your element for each of the ten craftwerks listed in step 2.
		- Step 5: Look at steps 3 and 4. Are there patterns in the ways the craftwerks use the element, and how do those relate to the problems they solve?
		- Step 6: Pick one of those patterns and describe it using the pattern template.
		- Step 7: You may repeat step 6 for each pattern you observed.
		- Ref Original
		  collapsed:: true
			- Step 1: Name a design element.
			- Step 2: Name ten games that use that element—the more different ways the games use it, the better.
			- Step 3: Describe how each of those games uses the element you chose. Try not to look for a pattern yet. Focus on accurately describing the way each game uses the element you identified.
			- Step 4: What design problems do the games use the element to solve? Some games may use the element for one purpose, while others use it for another. Many games use the elements in more than one way. Describe the problems solved by your element for each of the ten games listed in step 2.
			- Step 5: Look at steps 3 and 4. Are there patterns in the ways the games use the element, and how do those relate to the problems they solve?
			- Step 6: Pick one of those patterns and describe it using the pattern template.
			- Step 7: You may repeat step 6 for each pattern you observed.
	- ## Exercise 2: Higher-Order Patterns
		- Step 1: Name a design element.
		- Step 2: Name ten craftwerks that use that element—the more different ways the craftwerks use it, the better.
		- Step 3: Describe how each of those craftwerks uses the element you chose. Try not to look for a pattern yet. Focus on accurately describing the way each craftwerk uses the element you identified.
		- Step 4: What design problems do the craftwerks use the element to solve? Some craftwerks may use the element for one purpose, while others use it for another. Many craftwerks use the elements in more than one way. Describe the problems solved by your element for each of the ten craftwerks listed in step 2.
		- Step 5: Look at steps 3 and 4. Are there patterns in the ways the craftwerks use the element, and how do those relate to the problems they solve?
		- Step 6: Pick one of those patterns and describe it using the pattern template.
		- Step 7: You may repeat step 6 for each pattern you observed.
	-
