

class Page:
    def __init__(self, page_num, total_count, url_prefix, per_page, max_page=11):
        """
        :param page_num: 当前页码数
        :param total_count: 数据总数
        :param url_prefix: a标签href的前缀
        :param per_page: 每页的显示的数据数
        :param max_page: 页面上最多显示几个页码
        :使用方法: 注入上述参数后，获取数据起始，再获取HTML拼接代码
        """
        self.url_prefix = url_prefix
        # self.page_num = page_num
        # self.total_count = total_count
        # self.per_page = per_page
        # self.max_page = max_page
        # 总共需要多少页码来展示
        total_page, m = divmod(total_count, per_page)
        if m:
            total_page += 1
        self.total_page = total_page
        try:
            page_num = int(page_num)
            if page_num > total_page:
                page_num = total_page
        except Exception as e:
            page_num = 1
            print(e)
        self.page_num = page_num
        # 定义两个变量保存数据从哪儿取到哪儿
        self.data_start = (page_num - 1) * per_page
        self.data_end = page_num * per_page
        # 页面总共展示多少页码
        if total_page < max_page:
            max_page = total_page

        half_max_page = max_page // 2
        # 页面上展示的页码从哪儿开始
        page_start = page_num - half_max_page
        # 页面展示的页码从哪儿结束
        page_end = page_num + half_max_page
        # 如果当前页减一半 比1还小
        if page_start <= 1:
            page_start = 1
            page_end = max_page
        # 如果当前页加一半比总页码还大
        if page_end >= total_page:
            page_end = total_page
            page_start = total_page - max_page + 1
        self.page_start = page_start
        self.page_end = page_end

    @property
    def start(self):
        return self.data_start

    @property
    def end(self):
        return self.data_end
        # 当页展示的数据

    def page_html(self):
        html_str_list = ['<li><a href="{}?page=1">首页</a></li>'.format(self.url_prefix)]
        # 加上第一页和上一页按钮，如果为第一页，者上一页和首页不显示
        if self.page_num == 1:
            html_str_list.append(' <li style="display:none"><a href="{}?page={}">'
                                 '<span aria-hidden="true">&laquo;</span></a></li>'.format(self.url_prefix, self.page_num - 1))
        else:
            html_str_list.append(' <li><a href="{}?page={}">'
                                 '<span aria-hidden="true">&laquo;</span></a></li>'.format(self.url_prefix, self.page_num - 1))
        # 自行拼接HTML代码
        for i in range(self.page_start, self.page_end+1):
            if i == self.page_num:
                tmp = '<li class="active"><a href="{0}?page={1}">{1}</a></li>'.format(self.url_prefix, i)
            else:
                tmp = '<li><a href="{0}?page={1}">{1}</a></li>'.format(self.url_prefix, i)
            html_str_list.append(tmp)
        # 下一页按钮和最后一页的按钮，如果当前页是最后一页，则不显示下一页和尾页按钮
        if self.page_num >= self.total_page:
            html_str_list.append(' <li style="display:none"><a href="{}?page={}"><span aria-hidden="true">&raquo;'
                                 '</span></a></li>'.format(self.url_prefix, self.page_num+1))
        else:
            html_str_list.append(' <li><a href="{}?page={}"><span aria-hidden="true">&raquo;'
                                 '</span></a></li>'.format(self.url_prefix, self.page_num+1))
        html_str_list.append('<li><a href="{}?page={}">尾页</a></li>'.format(self.url_prefix, self.total_page))
        # 加上最后一页
        page_html = ''.join(html_str_list)
        return page_html

