from flask import render_template, flash, redirect, make_response
from app import app
from app.forms import TwitterHandleForm

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TwitterHandleForm()
    if form.validate_on_submit():
        # flash('Login requested for user {}, remember_me={}'.format(
            # form.twitterhandle.data, ))
        twitterhandle=form.twitterhandle.data
        return redirect('/piechart/{0}'.format(twitterhandle))
    return render_template('index.html', title='Home', form=form)

@app.route("/piechart/<twitterhandle>")
def pie(twitterhandle):



    
    from app.twitter_parser import twitter_parser as tp

    alltweets = tp.get_all_tweets(twitterhandle)
    word_dict = tp.word_count(alltweets)
    keywords_dict = tp.top10words(word_dict)

    

#     fig.suptitle('@' +str(user_name) + ' 10 Most Used Words on Twitter\n'+
#             str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
    values = [sizes for labels, sizes in keywords_dict]
    labels = [labels for labels, sizes in keywords_dict]
    colors = [ "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD",
            "#ABCABC", "#CAABB9", "#46F7F3", "#EFCDAB"]


    # Render the Template
    return render_template('pie.html', values=values, labels=labels,
            colors=colors, twitterhandle=twitterhandle)
