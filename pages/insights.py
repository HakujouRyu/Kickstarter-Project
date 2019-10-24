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
        
            ## What do we think?
            Could this be useful? Well, the short answer is: Maybe.  
            It's interesting to me that 'Category' rose to the top of the feature's importance list every time. 
            Sure, it makes sense in some ways, and we could speculate about who's on the internet, what categories are popular, etc. 
            But I don't think we could really formulate any conclusions on it from this data. 
            ## Speaking of Categories.
            ##### Let's talk features.
            As you saw on the front page, there are many aspects of a Kickstarter campaign that affect its outcome.
            We could not observe them all in the scope of this project, such as how popular the creator is, 
            how much money they spend on advertising, etc.
            There was plenty to look at still, and some of the other features that were shown to most heavily affect the model 
            were: 
            - Your goal; seems pretty straight forward. Is yours too lofty?
            - Days from creation to launch; How long did you give yourself to hype up your project once you created it's "draft?"
            - Campaign length; Kickstarter states that 30 days seems to be ideal for most.
            
            ## But how did we do?
            This is still a good dive into the subject, however.
            The baseline prediction accuracy rate of my 2019 data set was 57%.
            With this model, I was able to achieve an accuracy of 78%.
            """
        ),
        html.Img(src='assets/truepos_small.png', className='img-fluid'),
        
        dcc.Markdown(
            """
            Here, we see where the model was correct in its prediction that this project would be successful.
            By a large margin too. Note that the category of 'Video Games' carries a lot of weight!
 
            """
        ),
        html.Img(src='assets/true_neg_small.png', className='img-fluid'),
        
        dcc.Markdown(
            """
            Here, we see another correct example. 
            This time with the prediction that this project would fail.
            Though the model just barely got this wrong, it may be worth noting that the days to launch was 0.
            Would this project have been successful if they had spent more time tweaking the campaign publicly?
 
            """
        ),
        html.Img(src='assets/false_pos_small.png', className='img-fluid'),
        
        dcc.Markdown(
            """
            Here is an interesting example, The model predicted that this one would succeed but the project failed.
            Notice that the category even here was a big impact on the model's decision. Was it not enough, are we missing an angle,
             or are we over/undervaluing another feature?
 
            """
        ),
 
        dcc.Markdown(
            """
 
            ## Why so low? 
            Well, as I stated before, I think some of the biggest features would be your advertising and previous success and/or fame.
            ## What now?
            Good question! So, there is more I would like to do with this dataset!
            The creator could be discerned given enough time,
            and from there we could engineer a feature that is whether or not they have been successful in the past. 
            They may prove very predictive.
            Another feature that I did not get to engineer in my week of cleaning the blurb. 
            What does the creator say about their project? Using NLP we could see if some blurbs are suggested to be better than others. 
 
 
 
 
 
            """
        ),
    ],
    md=8,
)
 
 
column2 = dbc.Col(
    [
        html.Img(src='assets/small_importances.png', className='img-fluid'),
        dcc.Markdown(
            """These are the features used and their importances from tha latest iteration of the predictive model."""
        ),
        html.Img(src='assets/bigimportances.png', className='img-fluid'),
        dcc.Markdown(
            """ Here is what was passed to the very first iteration of the XGBClassifier that I used """
        )
 
    ]
)
 
layout = dbc.Row([column1, column2])

