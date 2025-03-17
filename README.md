# It's Not Good #ForYou
Isabella Heintges, B.S. in Electrical Engineering

## TikTok Algorithm Analysis: Social Media & Diet Culture
This repository contains all code used to analyze trends present in the data collected for my research on how TikTok's recommendation algorithm influences youth media consumption.

### Overview
With the growing popularity of TikTok, young audiences are increasingly looking to this application to seek and share health information, particulary in relation to topics of diet and fitness. The research, conducted as part of my case study, explores the extent to which TikTok's #ForYou algorithm amplifies diet-related content and its potential effects on young users' perceptions of health, diet, and body image.

### Research Context
This study examines how TikTok's reccomender system curates content streams based on user engagement, while determining whether this process results in the reinforcement of propogating negative health messages to young audiences. Further, this ingormation is used to explore the effects on adoloescent behaviors and perceptions of dieting and fitness. 

Generally, the research findings demonstrate:
- The test account, which interacted with diet-related content, was exposed to nine times more diet and fitness content than the control account.
- TikTok’s algorithm amplifies repetitive themes rather than moderating them, raising concerns about its potential role in reinforcing harmful health narratives.
- Algorithmic feedback loops create self-reinforcing exposure to specific narratives, potentially influencing young users' perceptions of body image and diet culture.

### Contents
- **control-hashtags.py** – Figure 2
  - Tracks the hashtags searched by the control account and their influence on content recommendations.
- **test-hashtags.py** – Figure 2
  - Investigates the hashtags searched by the test account and their role in shaping content exposure.
- **control-creators.py** – Figure 3
  - Analyzes the creators followed by the control account, including their engagement metrics.
- **test-creators.py** – Figure 4
  - Evaluates the creators followed by the test account and their content focus.
- **comparison-themes.py** – Figure 5
  - Compares the distribution of content themes between the control and test accounts.
- **cumulative-themes.py** – Figure 6
  - Aggregates the overall distribution of content themes recommended by TikTok’s algorithm.
- **cumulative-negative-per-day.py** – Figure 7
  - Analyzes daily fluctuations in negative content exposure across both accounts.
- **cumulative-negative-over-time.py** – Figure 8
  - Examines the cumulative exposure to negative content over the entire 10-day period for both accounts.
