from flask import Flask
from flask import render_template
import feedparser

app = Flask(__name__)

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"

@app.route("/")
def get_news():
    feed = feedparser.parse(BBC_FEED)
    first_article = feed['entries'][0]
    articles = feed['entries']
    # for a in articles:
    #     print(a.get("title"))

    return render_template("home.html", articles=feed['entries'])

    # return " "


    # return render_template("home.html",article=articles)

                            # title=first_article.get("title"),
                            # published = first_article.get("published"),
                            # summary = first_article.get("summary"))

    # html = []
    # html.append("""<html><body>""")
    # entries = feed['entries']
    # for e in entries:
    #     article="""
    #         <h1> BBC Headlines </h1>
    #         <b>{0}</b> <br/>
    #         <i>{1}</i> <br/>
    #         <p>{2}</p> <br/>""".format(e.get("title"),
    #                                    e.get("published"),
    #                                    e.get("summary"))
    #
    #     html.append(article)
    # html.append("""</body>
    #      </html>""")
    # result = ''.join(html)
    # return result


if __name__ == '__main__':
  app.run(port=5000, debug=True)