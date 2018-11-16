# coding:utf-8
# 因为之前的项目里面用到了whoosh,但是当时没有太多的耐心去看这个，这里深入的整理一下。
# whoosh是一个类似于博客的快速搜索项目，它可以实现快速的检索你想要的内容。
# 首先需要先安装whoosh. pip2 install whoosh
# quick_start
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser

schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
ix = create_in("indexdir", schema)  # 创建了一个对象，indexdir
writer = ix.writer()    # 一个写入对象
writer.add_document(title=u'First document', path=u"/a", content=u"This is the first document we've added!")    # 添加文档，里面是内容和路径以及文件名称。
writer.add_document(title=u'Second document', path=u"/b", content=u"The second one is even more interesting! ")  # 添加文档，里面是内容和路径以及文件名称。
writer.commit()     # 提交要添加的内容
with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse('first')  # 这里就会查找内容中包含first的, 类似re.compile
    results = searcher.search(query)  # 这里才是真正的执行查询操作
    print(results[0])
# result:   {"title": u"First document", "path": u"/a"}
# 上面这段代码并不能运行，运行会触发报错，但是可以简单的看到一些使用方法。

# 这些完全是根据现有经验推断出来的，实际情况，还需要看文档。

# The Index and Schema objects  # Index对象和Schema对象  也就是索引对象和概要对象

# To begin using Whoosh, you need an index object. The first time you create an index, you must define the index's schema.
# 在开始使用Whoosh之前，你需要创建一个index对象，创建index对象之前，你必须先定义一个索引的schema(概要/模式)
# The schema lists the fields in the index. A field is a piece of information for each document in the index, such as its title or text content.
# 该schema(概要/模式)列出了索引中的字段。字段是索引中每个文档的一条信息。就像标题或者文本内容一样。
# A field can be indexed(meaning it can be searched) and /or stored(meaning the value that gets indexed is returned with the results;
# 一个字段可以被索引(这意味着可以被查找) 或者被 存储起来(意味着值将会被查找到然后和结果一起返回。
# this is useful for fields such as the title)
# 这对于诸如标题的字段很有用
# example:
from whoosh.fields import Schema, TEXT
schema = Schema(title=TEXT, content=TEXT)

# You only need to do create the schema once, when you create the index. The schema is pickled and stored with the index.
# 你只需创建一次schema, 当你创建索引的时候，schema(概要/模式)被选中然后和索引一起存储起来。 ix = create_in("indexdir", schema)
# When you create the Schema object, you use keyword arguments to map field names to field types.
# 当你创建一个schema对象之后，你可以使用关键字参数将字段名称映射到字段类型.  (title=TEXT, content=TEXT)
# The list of fields and their types defines what you are indexing and what’s searchable.
# 字段列表和他们的类型决定了你将用什么去索引，以及什么是可以查找。
# Whoosh comes with some very useful predefined field types, and you can easily create your own.
# whoosh 预置了一些非常有用的字段类型，你也可以很容易的创建自己的字段类型。

# whoosh.fields.ID
# This type simply indexes (and optionally stores) the entire value of the field as a single unit
# 这种简单类型的索引是把字段的整个值(可选择存储)作为一个单元
# (that is, it doesn’t break it up into individual words). This is useful for fields such as a file path, URL, date, category, etc.
# 也就是说，它不会将其分解为单个单词）。这对于文件路径，URL，日期，类别等字段很有用。

# whoosh.fields.STORED
# This field is stored with the document, but not indexed. This field type is not indexed and not searchable.
# 这个字段将和文件一起存储，但是没有加入索引，这种字段类型没有编入索引并且不可搜索。
#  This is useful for document information you want to display to the user in the search results.
# 这对于在搜素结果中向用户展示文件信息很有用。
# whoosh.fields.KEYWORD
# This type is designed for space- or comma-separated keywords. This type is indexed and searchable (and optionally stored).
# 这种类型被设计用于空格隔开或者是逗号隔开的关键字。 这种类型是可以被索引和查找的(可以选择是否存储)
# To save space, it does not support phrase searching.
# 为了节省空间，这个不支持词组/短语查找。

# whoosh.fields.TEXT
# This type is for body text. It indexes (and optionally stores) the text and stores term positions to allow phrase searching.
# 这种类型用于正文.可以索引(可以被存储)文本和存储术语位置来允许短语/单词查找。

# whoosh.fields.NUMERIC
# This type is for numbers. You can store integers or floating point numbers.
# 这种类型用于存储数字。你可以存储整型或者浮点型的数字。

# whoosh.fields.BOOLEAN
# This type is for boolean (true/false) values.
# 这种类型用于存储布尔类型的值(True/False)

# whoosh.fields.DATETIME
# This type is for datetime objects. See Indexing and parsing dates/times for more information.
# 这种类型用于日期对象(datetime).查看索引和分解 日期/时间 来获取更多信息。

# whoosh.fields.NGRAM and whoosh.fields.NGRAMWORDS
# These types break the field text or individual terms into N-grams. See Indexing and searching N-grams for more information.
# 这些类型分解字段文本或单个术语分解成N-grames. 查看索引然后查找N-grams来获取更多信息。

# (As a shortcut, if you don’t need to pass any arguments to the field type, you can just give the class name and Whoosh will instantiate the object for you.)
# 一个捷径，如果你不需要传递任何参数给字段类型，你可以只提供一个类名，whoosh 将会实例化该对象。

from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT
schema = Schema(title=TEXT(stored=True), content=TEXT, path=ID(stored=True), tags=KEYWORD, icon=STORED)

# Once you have the schema, you can create an index using the create_in function:
# 当你有了schema之后，你可以用create_in来创建一个索引。

import os
from whoosh.index import create_inn

if not os.path.exists("index"):
    os.mkdir("index")
ix = create_in("index", schema)

# (At a low level, this creates a Storage object to contain the index.
# 在低版本上，这将创建一个存储对象来包含 索引.
#  A Storage object represents that medium in which the index will be stored. Usually this will be FileStorage, which stores the index as a set of files in a directory.)
# 一个存储对象表示在其中的索引将会被存储。通常会是文件存储——存储索引是一个目录里的文件集合。  # 这个不太会翻译，
# After you’ve created an index, you can open it using the open_dir convenience function:
# 当你创建一个索引之后，你可以用一个很容易的函数open_dir来打开索引。
from whoosh.index import open_dir

ix = open_dir("index")


# The IndexWriter object
# OK, so we’ve got an Index object, now we can start adding documents.
# 我们应该得到了索引对象，现在我们可以开始添加document了。
# The writer() method of the Index object returns an IndexWriter object that lets you add documents to the index.
# Index object 的 writer()方法将会返回一个IndexWriter对象来添加索引到documents中。
# The IndexWriter’s add_document(**kwargs) method accepts keyword arguments where the field name is mapped to a value:
# IndexWriter对象的add_document方法接受字段名和值一一映射的关键字参数

writer = ix.writer()
writer.add_document(title=u"My document", content=u"This is my document!",
                    path=u"/a", tags=u"first short", icon=u"/icons/star.png")
writer.add_document(title=u"Second try", content=u"This is the second example.",
                    path=u"/b", tags=u"second short", icon=u"/icons/sheep.png")
writer.add_document(title=u"Third time's the charm", content=u"Examples are many.",
                    path=u"/c", tags=u"short", icon=u"/icons/book.png")
writer.commit()

# Two important notes:
# You don’t have to fill in a value for every field. Whoosh doesn’t care if you leave out a field from a document.
# 你不需要将每一个字段都填上对应的值，如果你document里面漏掉了某个字段，whoosh也是ok的。
# Indexed text fields must be passed a unicode value. Fields that are stored but not indexed (STORED field type) can be passed any pickle-able object.
# 索引文本字段必须传一个unicode 的值，STORED字段类型(被存储但是不会被索引)
# 可以被传递任何可以被序列化的对象(list, set, tuple)(pickle-able 参见https://blog.csdn.net/funnyPython/article/details/84101699)
# If you have a text field that is both indexed and stored, you can index a unicode value but store a different object if necessary
# 如果你有一个可以被索引和存储的text字段，你可以索引一个unicode值.但是如果有必要，它会存储一个不同的对象
# (it’s usually not, but sometimes this is really useful) using this trick:
# 通常不会，但是有时候这个会很有用。看下面这个技巧。
# write.add_documents(title=u"Title to be indexed", _stored_title=u"Stored title")
# Calling commit() on the IndexWriter saves the added documents to the index:
# 调用IndexWriter对象的commit方法会将添加的文件保存到索引中。
# Once your documents are committed to the index, you can search for them.
# 一旦你的文档提交给了index,你就可以查找它们了。


# The Searcher object
# To begin searching the index, we’ll need a Searcher object:
# 开始查找索引前，我们需要一个Searcher对象。
searcher = ix.searcher()
# You’ll usually want to open the searcher using a with statement so the searcher is automatically closed when you’re done with it
# 你通常希望通过使用with关键字来打开searcher,这样当你用完后会自动关闭。
#  (searcher objects represent a number of open files,
# 搜索器对象代表了一些打开的文件
# so if you don’t explicitly close them and the system is slow to collect them, you can run out of file handles):
# 如果你没有明确关闭它们，系统会慢慢收集它们，这样会用光文件句柄的。
# with ix.searcher() as searcher:
#     ...
# This is of course equivalent to:
# 这种方式等同于
try:
    searcher = ix.searcher()
finally:
    searcher.close()

# The Searcher’s search() method takes a Query object. You can construct query objects directly or use a query parser to parse a query string.
# Searcher的search方法提供了一个查询对象。你可以直接构造一个查询对象来解析查询字符串。
# For example, this query would match documents that contain both “apple” and “bear” in the “content” field:
# 举一个例子，这个查询将匹配content中包含apple和bear的文件
# Construct query objects directly

from whoosh.query import *
myquery = And([Term("content", u"apple"), Term("content", "bear")])

# To parse a query string, you can use the default query parser in the qparser module.
# 为了解析查询字符串，你可以使用qparser模块里面默认查询解析器.
# The first argument to the QueryParser constructor is the default field to search.
# QueryParser构造器的第一个参数是要搜索的默认查找
# This is usually the “body text” field. The second optional argument is a schema to use to understand how to parse the fields:
# 这个通常是body text字段。第二个可选参数是schema用来理解如何解析字段的模式
# Parse a query string

from whoosh.qparser import QueryParser
parser = QueryParser("content", ix.schema)
myquery = parser.parse(querystring)

# Once you have a Searcher and a query object, you can use the Searcher‘s search() method to run the query and get a Results object:
# 当你有一个Searcher和一个查询对象，你可以使用Searcher的search方法在查询后获取一个Results对象。
# Parse a query string
"""
>>> results = searcher.search(myquery)
>>> print(len(results))
1
>>> print(results[0])
{"title": "Second try", "path": "/b", "icon": "/icons/sheep.png"}
"""
# The default QueryParser implements a query language very similar to Lucene’s.
# 默认QueryParser执行一个查询语句的方式和Lucene非常的相似。(Lucene 是一个基于 Java 的全文信息检索工具包.)
# It lets you connect terms with AND or OR, eleminate terms with NOT, group terms together into clauses with paredaintheses,
# 它允许您将查询语句与and 或者or与not进行连接。将查询语句组合成带括号的语句。
# do range, prefix, and wilcard queries, and specify different fields to search.
# 可以执行范围，前缀和wilcard查询，需要指定要搜索的不同字段。
# By default it joins clauses together with AND (so by default,
# 默认情况下，它用and将子句连接在一起（因此在默认情况下，
# all terms you specify must be in the document for the document to match):
# 你指定的所有的术语必须在文档中才能匹配。

"""
>>> print(parser.parse(u"render shade animate"))
And([Term("content", "render"), Term("content", "shade"), Term("content", "animate")])

>>> print(parser.parse(u"render OR (title:shade keyword:animate)"))
Or([Term("content", "render"), And([Term("title", "shade"), Term("keyword", "animate")])])

>>> print(parser.parse(u"rend*"))
Prefix("content", "rend")
"""

# Whoosh includes extra features for dealing with search results, such as
# Whoosh包含了处理查询结果的额外的功能。例如
# Sorting results by the value of an indexed field, instead of by .relelvance
# 按索引字段的值进行排序,而不是按照相关性排序。
# Highlighting the search terms in excerpts from the original documents.
# 在原始文档摘录中高亮查询搜索词。
# Expanding the query terms based on the top few documents found.
# 根据前几个少量的文档查询结果扩展查询条件。
# Paginating the results (e.g. “Showing results 1-20, page 1 of 4”).
# 分析结果（例如"显示结果1-20， 页数是1到4）

