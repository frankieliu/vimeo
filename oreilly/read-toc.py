from bs4 import BeautifulSoup as bs
with open("rails_toc.html",'r') as f:
    contents = f.read()
    soup = bs(contents,'lxml')
    for child in soup.recursiveChildGenerator():
        """
'class': ['content-ContentSummary-title']}, 'contents': ['Ruby on Rails 6: Summary'], 'parent': <a class="content-ContentSummary-link" href="/videos/ruby-on-rails/9780136733461/9780136733461-ROR6_15_00_00_00"><span class="content-ContentSummary-title">Ruby on Rails 6: Summary</span><div class="content-ProgressBar content-ProgressBar-isAnimated"><div class="content-ProgressBar-text"><span><span><span class="content-ContentSummary-completionIcon"><svg viewbox="5 5 14 14" xmlns="http://www.w3.org/2000/svg"><title>checkmark</title><path d="M9.79 15.29a1 1 0 0 0 1.41 0l5.54-5.54-1.5-1.5L10.5 13l-2.25-2.25-1.5 1.5z" style="fill: currentcolor;"></path></svg></span><span class="content-ContentSummary-progressText">44s</span></span></span></div></div></a>, 
        """
        if child.name == 'span':
            # print(child.__dict__)
            if 'class' in child.attrs:
                if child.attrs['class'][0] == 'content-ContentSummary-title':
                    print(child.contents[0])
                    print(child.parent.attrs['href'])
    #print(soup.prettify())
