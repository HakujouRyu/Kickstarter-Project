import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
 
from app import app
 
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            # Process
            ### What did I spend a week doing? 
            Cleaning mostly. When I first found this data set, I must admit, I was a little overzealous.
            I saw so much opportunity, I did not take the time to look to see how much work it would be to extract all of the data.
            ## Dirty Data?
            Well, some of the columns were in formats that presented challenges. It was exciting but time-consuming.
            ### The 'Dictionaries'
            Several of the columns were in what I thought to be dictionaries. 
            They were in fact JSON format, but some of them did not play nice with the JSON package native to python, so they ultimately got left alone.
            Something for me to revisit.
            ### Feature engineering.
            ##### Category
            So, I had a good hunch that the category of the project would be predictive, so I was sure to extract that out of the JSON formatted columns.
            When I did, I was left with the choice of which 'Category' identifier to keep. The model went crazy when it was given all of them. 
            Just barely beating baseline.
            The identifier I went with was "category_name" and the reason, besides retaining predictive power,  was two-fold. 
            One, I wanted a simple model that could be easily manipulated and interpreted by the user. 
            Two I wanted to keep as much of the diverse info as possible from that group of features.
            This allowed me to create an easy to read if long, drop-down of options to choose from. 
            If I were not going to put this in an app like this, I would have also kept one of the parent category features.
            ##### The dates
            The dates we are given in this dataset are 'created', 'launched', and 'deadline'. 
            From there, I converted them into a readable format and created more features. 
            I created the campaign length, days_to_launch, which ended up being very important to the model. 
            It's simple, but I was pretty happy to see that days to launch was useful. 
            I had only recently learned that you could create and share a project on Kickstarter before actually launching it.
            This gives you time to advertise, and to let the community help you work out perks, and goals. 
            The other features I created were the month, day, year, and day name of the launch and deadline dates.
            My intuition was that some times of the month/year would significantly increase your odds of success. 
            This did not hold true, however.
            ##### International
            "Sir Not Appearing in this Film" There was a column that held more predictive power than some of the ones that made the cut, 
            and the column was 'usd_type'. The binary values of this column were 'domestic' and 'international'. It is unclear whether this meant that the creator allowed 
            shipping overseas or if this was a project that originated overseas, as there were many observations that overlapped. 
            Though, I suspect that there should not have been.
 
            ### XGBClassifier 
            I chose a tree-based model because I really like the feature interaction detection that comes baked into them. 
            Though, given the amount of time I spent training and retraining my models, I think that I should work with a non-boosted model first next time.
            Just until I get the results that I want, then take my best few cases to the boosted model to see what is best.
            This may end up saving me time. Precious time I can spend on EDA.
 
            """
        ),
 
    ],
)
 
layout = dbc.Row([column1])

