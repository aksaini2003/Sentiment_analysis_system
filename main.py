    #lets also make a function for performing the preprocessing as we have done on the training dataset 
import string 
import re
import joblib 
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
def preprocessing(text):  
        pattern=r'<.*?>' 
        pattern=re.compile(pattern)
        # def remove_tags(text):
        #for removing the html tags from the given text as input for the prediction 

        text=pattern.sub('',text)
            # return text
        # df['review']=df['review'].apply(remove_tags)
        pattern=r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        pattern=re.compile(pattern)
        # def remove_url(text):
        #for removing the urls from the given text 

        text=pattern.sub('',text)
            # return text 
        
        punc=string.punctuation 
        # print(punc)
        # def remove_punc(text):
        #for removing the punctuation from the given text 

        for i in punc:
                if i in text:
                    text=text.replace(i,'')
            # return text 
        #lets load the slang_dictionary for removing the slangs 
        slangs=joblib.load('slang_dictionary.pkl')
        for slang, meaning in slangs.items():
                text = re.sub(r'\b' + re.escape(slang) + r'\b', meaning, text)
            # return text
        # print(tb.correct().string)
        # def spe_corr(text): spelling correction
        tb=TextBlob(text)
        text=tb.correct().string 
            # return text
        

        # Download the NLTK stopwords corpus
        

        # def remove_stopwords(text):
        #for removing the stop words

            # Tokenize the text
        words = text.split()

            # Get the list of English stopwords
        stop_words = set(stopwords.words('english'))

            # Remove stopwords
        filtered_words = [word for word in words if word.lower() not in stop_words]

            # Return the filtered text
        text=" ".join(filtered_words)
        #lets also transform the whole dataset into the tfidf vecotrization
        tfv=joblib.load('tfidf_vectorizer.pkl')
        text=tfv.transform([text]).toarray()
        #these all the preprocessing steps that we have to perform on the given input data 
        return text 
#lets also make the function that takes the data and return the prediction 
def predict_(text):
    lr=joblib.load('log_reg_model.pkl')
    pred=lr.predict(text)
    #lets do the prediction by loading the models that we have saved 
    
    if pred==1:
        return 'POSITIVE SENTIMENTS'
    else:
        return 'NEGATIVE SENTIMENTS'
#lets do the prediction 
text='''Okay, last night, August 18th, 2004, I had the distinct displeasure of meeting Mr. Van Bebble at a showing of the film The Manson Family at the Three Penny in Chicago as part of the Chicago Underground Film Festival. Here's what I have to say about it. First of all, the film is an obvious rip off of every Kenneth Anger, Roman Polanski, Oliver Stone and Terry Gilliam movie I've ever seen. Second of all, in a short Q & A session after the show Mr. Van Bebble immediately stated that he never made any contact with the actual Manson Family members or Charlie himself, calling them liars and saying he wanted nothing to do with them, that the film was based on his (Van Bebble's) take on the trial having seen it all from his living room on TV and in the news (and I'm assuming from the Autobiography and the book Helter Skelter which were directly mimicked through the narrative). So I had second dibs on questions, I asked if he was trying to present the outsider, Mtv, sex drugs and rock 'n roll version and not necessarily the true story. This question obviously pissed off the by now sloshed director who started shouting ""f*** you, shut the f*** up, this is the truth! All those other movies are bullsh**!""<br /><br />Well anyway, I didn't even think about how ridiculous this was until the next day when I read the tagline for the film, ""You've heard the laws side of the story...now hear the story as it is told by the Manson Family."" Excuse me, if this guy has never even spoken to the family and considers them to be liars that he doesn't want to have anything to do with, how in God's name can he tell the story for them!? This is the most ridiculous statement I have ever heard! The film was obviously catered to the sex drugs and rock 'n roll audience that it had no trouble in attracting to the small, dimly lit theatre, and was even more obviously spawned by the sex drugs and rock 'n roll mind of a man who couldn't even watch his own film without getting up every ten minutes to go get more beer or to shout some sort of Rocky Horroresque call line to the actors on screen. This film accomplishes little more than warping the public's image of actual events (which helped shape the state of America and much of the world today) into some sort of Slasher/Comic Book/Porno/Rape fantasy dreamed up by an obviously shallow individual.<br /><br />The film was definitely very impressive to look at. The soundtrack was refreshing as it contained actual samples of Charlie's work with the Family off of his Lie album. The editing was nice and choppy to simulate the nauseating uncertainty of most modern music videos. All in all this film would have made a much better addition to the catalogues at Mtv than to the Underground Film Festival or for that matter the minds of any intellectual observers. I felt like I was at a midnight Rocky Horror viewing the way the audience was dressed and behaving (probably the best part of the experience). The cast was very good with the exception of Charlie who resembled some sort of stoned Dungeons and Dragons enthusiast more than the actual role he was portraying. The descriptions the film gave of him as full of energy, throwing ten things at you and being very physical about it all the while did not match at all the slow, lethargic, and chubby representation that was actually presented.<br /><br />All in all the film basically explains itself as Sadie (or maybe it was Linda) declares at the end, ""You can write a bunch of bullsh** books or make a bunch of bullsh** movies...etc. etc."" Case in point. Even the disclaimer ""Based on a True Story"" is a dead giveaway, signalling that somewhere beneath this psychedelic garbage heap lay the foundation of an actual story with content that will make and has made a difference in the world. All you have to do is a little bit of alchemy to separate the truth from the the crap, or actually, maybe you could just avoid it all together and go read a book instead.<br /><br />All I can say is this, when the film ended I got a free beer so I'm glad I went, but not so glad I spent fifteen dollars on my ticket to be told to shut the f*** up for asking the director a question. Peace.'''
print(predict_(preprocessing(text)))