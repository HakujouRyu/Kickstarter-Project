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
            Could this be useful? Well, short answer is: Maybe.  
            It's interesting to me that 'Category' rose to the top of the feature's importance list everytime. 
            Sure, it makes sense in some ways, and we could speculate about who's on the internet, what categories are popular, etc. 
            But I don't think we could really formulate any conclusions on it from this data. 
            ## Speaking of Categories.
            [Permutation_Importance](assets\\bigimportances.png){: .center-block :}
            ##### Let's talk features.
            As you saw on the front page, there are many aspects of a Kickstarter campaign that affect it's outcome.
            We could not observe them all in the scope of this project, such as how popular the creator is, 
            how much money they spend on advertising, etc.
            There was plenty to look at still, and some of the other features that were shown to most heavily effect the model 
            were: 
            - Your goal; seems pretty straight forward. Is yours too lofty?
            - Days from creation to launch; How long did you give yourself to hype up your project once you created it's "draft?"
            - Campaing length; Kickstarter states that 30 days seems to be ideal for most.
            
            ## But how did we do?
            This is still a good dive into the subject, however.
            The baseline prediction accuracy rate of my 2019 data set was 57%.
            With this model, I was able to achieve an accuracy of 78%.
            ## Why so low? 
            Well, as I stated before, I think some of the biggest features would be your advertising and previous success and/or fame.
            ## What now?
            Good question! So, there is more I would like to do with this dataset!
            The creator could be discerned given enough time,
            and from there we could engineer a feature that is whether or not they have been successful in the past. 
            They may prove very predictive.
            Another feature that I did not get to engineer in my week of cleaning the blurb. 
            What does the creator say about their project? Using NLP we could see if some blurbs are sugeested to be better than others. 





            """
        ),
    ],
    md=12,
)


column2 = dbc.Col(
    [
        
    ]
)

layout = dbc.Row([column1])