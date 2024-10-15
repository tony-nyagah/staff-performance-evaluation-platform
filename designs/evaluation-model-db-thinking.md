## What is this?
Here I try to look at how the current Excel file used for performance evaluation is structured and how this can transfer into Django models and views.

## The current situation
### Scoring
The Excel file used for appraisal as of the writing of this is made up of various sections each allowing staff make comments and score themselves. The scores go from 0.00 to 5.00.    
Managers can then add comments and scores alongside the staff's score. They can do this only for staff they supervise.    
The scores are as follow:
* Development required / Poor role fit: 0 - 1.29
* Improvement required: 1.3 - 2.54
* Achieved: 2.55 - 4.29
* Exceptional: 4.3 - 4.79
* Distinguished: 4.8 - 5.00    

There is a final percentage score calculated for each section that uses this formula in the Excel sheet: `=(SUM(M29:M36)/(COUNT(M29:M36,"<>0")*5)*20/100)`.    
The score is calculated for both the manager's scores and the staff's scores. The resultant scores are a percentage.    
The scores are rated as:
* Development required / Poor role fit: 0 - 49%
* Improvement required: 50 - 69%
* Achieved: 70 - 85%
* Exceptional: 86 - 100%
* Distinguished: above 100%

### Sections
The sections and what they need submitted are:

**Section 1: Review Key Performance Indicators**

These are your previous year's goals. The fields to fill in are:
* Goal - text
* KPI - On hold, ongoing or achieved with a comment from the user should include percentages if possible
* Staff comments - The staff's comment
* Staff score - The score the staff has given themselves
* Supervisor comment - The supervisor's comment on the goal
* Manager score - The supervisor's score on the goal
* Review Key Performance Indicators Percentage Score - The final percentage score of the manager's scores 

**Section 2: Commitment To The Organization**
These are common commitment areas that are important to the company as outlined in company policy. the fields to fill are:

* Commitment areas - These are stated by the organization
* KPI - A score of 0.00 to 5.00. Filled in by the staff
* Staff comments - Further comments by the staff on the commitment area
* Staff score - A score given by the staff i regards to what they think their commitment to an area is. Can be from 0.00 to 5.00.
* Supervisor comments - The supervisor's comments on the commitment area
* Manager score - The supervisor's score on the commitment area

**Section 3: Team Cohesion and Leadership Ability**
In this section, the staff member is rated by themselves, a supervisor, a peer and a subordinate. The existing fields are:

* Title and Relationship: There's self-review, supervisor, peer and subordinate
* Strengths: The staff's strengths
* Weaknesses: The staff's weaknesses
* Recommended targets/achievements: Recommendations for targets for next year
* Score: The score whoever is reviewing gives you

**Section 4: Personal and Professional Development and Initiatives**
In this section, the staff lists and comments on personal and professional achievements and contributions that are relevant to the business. This includes courses or activities completed in the year.
The existing fields are;

* Achievements or contribution: The relevant achievement and contribution. This is text
* Staff comments: The comments by the staff on this achievement
* Staff score: The score that the staff gives to their achievement/contribution
* Supervisor comments: The supervisor's comment
* Manager score: The supervisor's score

**Section 5: Overall Performance**
The overall performance. The fields are:

* Staff/Employee Score: an average of scores in the staff's scores in Personal and Professional Development and Initiatives section, Review Key Performance Indicators section, Commitment To The Organization section and Team Cohesion and Leadership Ability section.
* Manager/Supervisor Score: an average of the manager's/supervisor's scores in Personal and Professional Development and Initiatives section, Review Key Performance Indicators section, Commitment To The Organization section and Team Cohesion and Leadership Ability section.
* Overall Score: the sum of the manager's scores in Personal and Professional Development and Initiatives section, Review Key Performance Indicators section, Commitment To The Organization section and Team Cohesion and Leadership Ability section.
* Performance Ranking: Check the overall score and give it a named grading:
  * Overall score >= 96% = DISTINGUISHED
  * Overall score >= 86% = EXCEPTIONAL
  * Overall score >= 51% = ACHIEVER
  * Overall score >= 26% = IMPROVEMENT REQUIRED, DEVELOPMENT REQUIRED/ POOR ROLE FIT

**Section 6: Feedback**
Feedback section. Mostly just text. The fields are:

* Employee feedback
* Supervisor feedback

**Upcoming year's goals**
With reference to the position responsibilities, list below the goals, objectives, projects or special assignments which should be continued and/or completed in the coming year.  It is understood that these goals, objectives, etc. are subject to adjustment or change as situations and priorities change.  This section should be detached and kept in departmental files so that it can be updated as the situation warrants and so that it can be used to assist the rater at the end of the next evaluation period.  

There are employee goals and suggested goals. The suggested goals are given by the manager and add on or improve on the employee's goals.

The fields are:

* Employee goals
* Supervisor goals

These goals are what will be reviewed the next year.

**Training needs identified for the coming year**
These are training needs the employee has identified for themselves or their team.