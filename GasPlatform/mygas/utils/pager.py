class PageInfo(object):

    def __init__(self,current_page,all_count,per_page,base_url,show_page=11):
        try:
          self.current_page = int(current_page)
        except Exception:
            self.current_page = 1
        self.per_page = per_page
        a,b = divmod(all_count,per_page)
        if b:
          a = a+1
        self.all_pager = a
        self.show_page = show_page
        self.base_url = base_url

    def start(self):
        return (self.current_page-1)*self.per_page

    def end(self):
        return (self.current_page)*self.per_page

    def pager(self):
        # v = "<a href='/custom/?page=1/'>1</a>""<a href='/custom/?page=2/'>2</a>"
        # return v
        page_list=[]


        half = int((self.show_page-1)/2)

        if self.all_pager < self.show_page:
            begin = 1
            stop = self.all_pager+1
        else:
            if self.current_page <= half:
                begin = 1
                stop = self.show_page+1
            else:
                if self.current_page + half >self.all_pager:
                    begin = self.all_pager-self.show_page+1
                    stop = self.all_pager +1
                else:
                    begin = self.current_page-half
                    stop = self.current_page+half+1

        if self.current_page <= 1:
           prev = "<li><a href='#'>上一页</a></li>"
        else:
           prev = "<li><a href='%s?page=%s'>上一页</a></li>"%(self.base_url,self.current_page-1)
        page_list.append(prev)

        for i in range(begin,stop):
            if i == self.current_page:
                temp = "<li class='active'><a href='%s?page=%s'>%s</a></li>"%(self.base_url,i,i)
            else:
                temp = "<li><a href='%s?page=%s'>%s</a></li>"%(self.base_url,i,i)
            page_list.append(temp)

        if self.current_page >= self.all_pager:
           nex = "<li><a href='#'>下一页</a></li>"
        else:
           nex = "<li><a href='%s?page=%s'>下一页</a></li>"%(self.base_url,self.current_page+1)
        page_list.append(nex)

        return ''.join(page_list)     #列表里的每个元素拼接