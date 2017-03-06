#!/usr/bin/python
# -*- coding: UTF-8 -*-

'文档注释:a test module'
__author__ = 'chlma'

# 1.确定URL并抓取页面代码

import urllib
import urllib2

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    print response.read()
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason

print url

'''/System/Library/Frameworks/Python.framework/Versions/2.6/bin/python2.6 /Users/machunlei/Documents/MyPythonStudy/爬虫系列/demo4.py
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<meta http-equiv="X-UA-Compatible" content="chrome=1,IE=edge">
<meta name="renderer" content="webkit"/>
<meta name="applicable-device" content="pc">
<title>













24小时爆笑笑话大全 - 糗事百科
</title>

















<meta name="keywords" content="笑话,笑话大全" />
<meta name="description" content="糗事百科官网提供24小时最糗搞笑笑话大全,糗百24小时内最新最糗事就只在糗事百科官网24小时专题,囊括恶搞、最尴尬糗事精华,快乐减压！"/>

<meta http-equiv="mobile-agent" content="format=xhtml;url=http://www.qiushibaike.com/">
<meta http-equiv="mobile-agent" content="format=html5;url=http://www.qiushibaike.com/">




<meta name="robots" content="noarchive">
<link href="http://static.qiushibaike.com/css/dist/web/app.min.css?v=f9ad525ffb58b06294fc6212976ceb5e" media="screen, projection" rel="stylesheet" type="text/css"/>
<script type="text/javascript">
// Baidu Automatic push content
var _hmt = _hmt || [];
(function() {
var hm = document.createElement("script");
hm.src = "https://hm.baidu.com/hm.js?2670efbdd59c7e3ed3749b458cafaa37";
var s = document.getElementsByTagName("script")[0];
s.parentNode.insertBefore(hm, s);
})();
</script>
</head>
<body>


<div id="header" class="head">
<div class="content-block">
<div class="logo" id="hd_logo">
<a href="/"><h1>糗事百科</h1></a>
</div>
<div id="menu" class="menu-bar menu clearfix" style="margin:0 10px">
<a  href="/" rel="nofollow">热门</a>
<a  id="highlight"  href="/hot/">24小时</a>
<a  href="/imgrank/">热图</a>
<a  href="/text/">文字</a>
<a  href="/history/">穿越</a>
<a  href="/pic/">糗图</a>
<a  href="/textnew/">新鲜</a>
<a  class="fn-signin-required" href="javascript:void(0);" data-go="/article/add" rel="nofollow">投稿</a>
<!--<a href="http://www.youliaodao.cn" target="_blank" rel="nofollow">百科</a>-->
</div>

<div class="userbar clearfix">
<div class="login hidden">
<a href="/my" class="username" id="uname" rel="nofollow"></a>
</div>
<div class="logout">
<a href="javascript:void(0);" class="fn-signin-required logintop" id='logintop' rel="nofollow" style="font-size:16.5px;">登录</a>
</div>
</div>

</div>
</div>



<div id="content" class="main">
<div class="content-block clearfix">

<div id="content-left" class="col1">



<div class="article block untagged mb15" id='qiushi_tag_118650553'>

<div class="author clearfix">
<a href="/users/22891657/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/2289/22891657/medium/20150227170003.jpg" alt="球白球白"/>
</a>
<a href="/users/22891657/" target="_blank" title="球白球白">
<h2>球白球白</h2>
</a>
<div class="articleGender manIcon">30</div>
</div>



<a href="/article/118650553" target="_blank" class='contentHerf' >
<div class="content">



<span>我问我同学：“听说你的感情路不顺？”<br/>同学说：“很顺啊，一路上都没有什么人。”<br/>我..........</span>


</div>
</a>





<div class="stats">
<span class="stats-vote"><i class="number">8618</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/118650553" data-share="/article/118650553" id="c-118650553" class="qiushi_comments" target="_blank">
<i class="number">127</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_118650553" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118650553" class="up">
<a href="javascript:voting(118650553,1)" class="voting" data-article="118650553" id="up-118650553" rel="nofollow">
<i></i>
<span class="number hidden">8768</span>
</a>
</li>
<li id="vote-dn-118650553" class="down">
<a href="javascript:voting(118650553,-1)" class="voting" data-article="118650553" id="dn-118650553" rel="nofollow">
<i></i>
<span class="number hidden">-150</span>
</a>
</li>

<li class="comments">
<a href="/article/118650553" id="c-118650553" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>




</div>








<div class="article block untagged mb15" id='qiushi_tag_118661060'>

<div class="author clearfix">
<a href="/users/31167196/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/3116/31167196/medium/201701230755037.JPEG" alt="脑补的傻娇啊～"/>
</a>
<a href="/users/31167196/" target="_blank" title="脑补的傻娇啊～">
<h2>脑补的傻娇啊～</h2>
</a>
<div class="articleGender womenIcon">13</div>
</div>



<a href="/article/118661060" target="_blank" class='contentHerf' >
<div class="content">



<span>小时候闯祸了，被老妈打哭了。<br/>然后我哭的时候看了一眼镜子，发现自己好滑稽，就噗嗤一声笑了出来……<br/>然后，我妈又重新打了我一顿……</span>


</div>
</a>





<div class="stats">
<span class="stats-vote"><i class="number">7216</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/118661060" data-share="/article/118661060" id="c-118661060" class="qiushi_comments" target="_blank">
<i class="number">132</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_118661060" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118661060" class="up">
<a href="javascript:voting(118661060,1)" class="voting" data-article="118661060" id="up-118661060" rel="nofollow">
<i></i>
<span class="number hidden">7338</span>
</a>
</li>
<li id="vote-dn-118661060" class="down">
<a href="javascript:voting(118661060,-1)" class="voting" data-article="118661060" id="dn-118661060" rel="nofollow">
<i></i>
<span class="number hidden">-122</span>
</a>
</li>

<li class="comments">
<a href="/article/118661060" id="c-118661060" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>




<a href="/article/118661060" class='indexGodCmt' onclick="_hmt.push(['_trackEvent','web_list_god','chick'])" rel="nofollow" target='_blank' >
<div class="cmtMain">
<span class="cmt-god" ></span>

<span class="cmt-name">轮椅</span>

<div class="main-text">
：回复 59楼：管我吊事？？
<div class="likenum">
<img src="http://static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad" />


31

</div>
</div>
</div>
</a>



</div>








<div class="article block untagged mb15" id='qiushi_tag_118658175'>

<div class="author clearfix">
<a href="/users/23331917/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/2333/23331917/medium/2017030216145091.JPEG" alt="傻晴°"/>
</a>
<a href="/users/23331917/" target="_blank" title="傻晴°">
<h2>傻晴°</h2>
</a>
<div class="articleGender womenIcon">25</div>
</div>



<a href="/article/118658175" target="_blank" class='contentHerf' >
<div class="content">



<span>结婚时问弟弟:姐结婚了以后要是受欺负。你可要帮姐姐啊！<br/>弟弟上下瞄了我两眼:就你这方头大脸，五大三粗的样子，姐夫要是敢欺负你。我便敬他是条汉子……</span>


</div>
</a>





<div class="stats">
<span class="stats-vote"><i class="number">10117</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/118658175" data-share="/article/118658175" id="c-118658175" class="qiushi_comments" target="_blank">
<i class="number">113</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_118658175" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118658175" class="up">
<a href="javascript:voting(118658175,1)" class="voting" data-article="118658175" id="up-118658175" rel="nofollow">
<i></i>
<span class="number hidden">10296</span>
</a>
</li>
<li id="vote-dn-118658175" class="down">
<a href="javascript:voting(118658175,-1)" class="voting" data-article="118658175" id="dn-118658175" rel="nofollow">
<i></i>
<span class="number hidden">-179</span>
</a>
</li>

<li class="comments">
<a href="/article/118658175" id="c-118658175" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>




<a href="/article/118658175" class='indexGodCmt' onclick="_hmt.push(['_trackEvent','web_list_god','chick'])" rel="nofollow" target='_blank' >
<div class="cmtMain">
<span class="cmt-god" ></span>

<span class="cmt-name">胖香</span>

<div class="main-text">
：小舅子质疑姐夫不是条汉子？！[面瘫神]这个6，如果我是姐夫，小舅子一定会后悔说过这么一段话的，，[奸笑]
<div class="likenum">
<img src="http://static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad" />


46

</div>
</div>
</div>
</a>



</div>








<div class="article block untagged mb15" id='qiushi_tag_118649944'>

<div class="author clearfix">
<a href="/users/30880816/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/3088/30880816/medium/201702281929007.JPEG" alt="【星空】棒棒"/>
</a>
<a href="/users/30880816/" target="_blank" title="【星空】棒棒">
<h2>【星空】棒棒</h2>
</a>
<div class="articleGender manIcon">35</div>
</div>



<a href="/article/118649944" target="_blank" class='contentHerf' >
<div class="content">



<span>记得那是一个冬天的夜晚，我脱脱穿穿了十几次毛衣！<br/>因为儿子要看黑夜里静电发出的光亮！</span>


</div>
</a>





<div class="stats">
<span class="stats-vote"><i class="number">9920</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/118649944" data-share="/article/118649944" id="c-118649944" class="qiushi_comments" target="_blank">
<i class="number">224</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_118649944" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118649944" class="up">
<a href="javascript:voting(118649944,1)" class="voting" data-article="118649944" id="up-118649944" rel="nofollow">
<i></i>
<span class="number hidden">10103</span>
</a>
</li>
<li id="vote-dn-118649944" class="down">
<a href="javascript:voting(118649944,-1)" class="voting" data-article="118649944" id="dn-118649944" rel="nofollow">
<i></i>
<span class="number hidden">-183</span>
</a>
</li>

<li class="comments">
<a href="/article/118649944" id="c-118649944" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>




<a href="/article/118649944" class='indexGodCmt' onclick="_hmt.push(['_trackEvent','web_list_god','chick'])" rel="nofollow" target='_blank' >
<div class="cmtMain">
<span class="cmt-god" ></span>

<span class="cmt-name">【星空】小静</span>

<div class="main-text">
：你是电，你是光，你是唯一的制杖～
<div class="likenum">
<img src="http://static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad" />


373

</div>
</div>
</div>
</a>



</div>








<div class="article block untagged mb15" id='qiushi_tag_118664571'>

<div class="author clearfix">
<a href="/users/19662467/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/1966/19662467/medium/20141127164909.jpg" alt="哈嘿2014"/>
</a>
<a href="/users/19662467/" target="_blank" title="哈嘿2014">
<h2>哈嘿2014</h2>
</a>
<div class="articleGender manIcon">29</div>
</div>



<a href="/article/118664571" target="_blank" class='contentHerf' >
<div class="content">



<span>结婚前，看到媳妇，总是想上辈子修的什么福，找到这么温柔贤惠的女朋友。结婚后，他娘的这是上辈子造的什么孽，摊上这么个娘们</span>


</div>
</a>





<div class="stats">
<span class="stats-vote"><i class="number">5481</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/118664571" data-share="/article/118664571" id="c-118664571" class="qiushi_comments" target="_blank">
<i class="number">134</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_118664571" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118664571" class="up">
<a href="javascript:voting(118664571,1)" class="voting" data-article="118664571" id="up-118664571" rel="nofollow">
<i></i>
<span class="number hidden">5582</span>
</a>
</li>
<li id="vote-dn-118664571" class="down">
<a href="javascript:voting(118664571,-1)" class="voting" data-article="118664571" id="dn-118664571" rel="nofollow">
<i></i>
<span class="number hidden">-101</span>
</a>
</li>

<li class="comments">
<a href="/article/118664571" id="c-118664571" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>




<a href="/article/118664571" class='indexGodCmt' onclick="_hmt.push(['_trackEvent','web_list_god','chick'])" rel="nofollow" target='_blank' >
<div class="cmtMain">
<span class="cmt-god" ></span>

<span class="cmt-name">-猜猜我是谁-</span>

<div class="main-text">
：说这话居然敢不匿名？我就静静地看着楼主烧完头七、二七、三七、四七、五七、六七、七七，接下来就是周年、二周年、三周年……
<div class="likenum">
<img src="http://static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad" />


74

</div>
</div>
</div>
</a>



</div>








<div class="article block untagged mb15" id='qiushi_tag_118652790'>

<div class="author clearfix">
<a href="/users/33285483/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/3328/33285483/medium/2017011123451060.JPEG" alt="＆将心比心"/>
</a>
<a href="/users/33285483/" target="_blank" title="＆将心比心">
<h2>＆将心比心</h2>
</a>
<div class="articleGender womenIcon">47</div>
</div>



<a href="/article/118652790" target="_blank" class='contentHerf' >
<div class="content">



<span>新抱回来的小狗闺女在训练它往回捡东西，表现不错，嗖嗖的捡回来了，就是死活不撒嘴，不给我们，这二货也不是哈士奇，咋也这么蠢萌蠢萌的</span>


</div>
</a>




<div class="thumb">

<a href="/article/118652790" target="_blank">
<img src="http://pic.qiushibaike.com/system/pictures/11865/118652790/medium/app118652790.jpg" alt="这二货也不是哈士奇" />
</a>

</div>



<div class="stats">
<span class="stats-vote"><i class="number">398</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/118652790" data-share="/article/118652790" id="c-118652790" class="qiushi_comments" target="_blank">
<i class="number">16</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_118652790" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118652790" class="up">
<a href="javascript:voting(118652790,1)" class="voting" data-article="118652790" id="up-118652790" rel="nofollow">
<i></i>
<span class="number hidden">402</span>
</a>
</li>
<li id="vote-dn-118652790" class="down">
<a href="javascript:voting(118652790,-1)" class="voting" data-article="118652790" id="dn-118652790" rel="nofollow">
<i></i>
<span class="number hidden">-4</span>
</a>
</li>

<li class="comments">
<a href="/article/118652790" id="c-118652790" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>




</div>








<div class="article block untagged mb15" id='qiushi_tag_118661644'>

<div class="author clearfix">
<a href="/users/31133782/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/3113/31133782/medium/20160206084916.jpg" alt="墨随轻"/>
</a>
<a href="/users/31133782/" target="_blank" title="墨随轻">
<h2>墨随轻</h2>
</a>
<div class="articleGender manIcon">18</div>
</div>



<a href="/article/118661644" target="_blank" class='contentHerf' >
<div class="content">



<span>上厕所，小便完了，想了想有感觉了要大便。就又脱裤子蹲下来，旁边一哥们的说；行啊，兄弟！讲究啊，上个厕所还分两步走。</span>


</div>
</a>





<div class="stats">
<span class="stats-vote"><i class="number">6320</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/118661644" data-share="/article/118661644" id="c-118661644" class="qiushi_comments" target="_blank">
<i class="number">89</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_118661644" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118661644" class="up">
<a href="javascript:voting(118661644,1)" class="voting" data-article="118661644" id="up-118661644" rel="nofollow">
<i></i>
<span class="number hidden">6440</span>
</a>
</li>
<li id="vote-dn-118661644" class="down">
<a href="javascript:voting(118661644,-1)" class="voting" data-article="118661644" id="dn-118661644" rel="nofollow">
<i></i>
<span class="number hidden">-120</span>
</a>
</li>

<li class="comments">
<a href="/article/118661644" id="c-118661644" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>




</div>








<div class="article block untagged mb15" id='qiushi_tag_118662694'>

<div class="author clearfix">
<a href="/users/12400419/" target="_blank" rel="nofollow">
<img src="http://static.qiushibaike.com/images/thumb/missing.png" alt="长不大的老叔叔"/>
</a>
<a href="/users/12400419/" target="_blank" title="长不大的老叔叔">
<h2>长不大的老叔叔</h2>
</a>
<div class="articleGender manIcon">34</div>
</div>



<a href="/article/118662694" target="_blank" class='contentHerf' >
<div class="content">



<span>小时候发育比女生晚，女生一个个生猛得很，我嘛，打不过她们却还喜欢欺负她们，每次被女生追到男厕所，直到我脱掉裤子，捏起小丁丁朝她们恐吓，她们才捂着脸跑开，尼玛，现在同学聚会，她们说班上那么多男生，唯有我的丁丁全年级女生都看到过，真想抹掉那段历史</span>


</div>
</a>





<div class="stats">
<span class="stats-vote"><i class="number">4936</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/118662694" data-share="/article/118662694" id="c-118662694" class="qiushi_comments" target="_blank">
<i class="number">199</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_118662694" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118662694" class="up">
<a href="javascript:voting(118662694,1)" class="voting" data-article="118662694" id="up-118662694" rel="nofollow">
<i></i>
<span class="number hidden">5032</span>
</a>
</li>
<li id="vote-dn-118662694" class="down">
<a href="javascript:voting(118662694,-1)" class="voting" data-article="118662694" id="dn-118662694" rel="nofollow">
<i></i>
<span class="number hidden">-96</span>
</a>
</li>

<li class="comments">
<a href="/article/118662694" id="c-118662694" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>




<a href="/article/118662694" class='indexGodCmt' onclick="_hmt.push(['_trackEvent','web_list_god','chick'])" rel="nofollow" target='_blank' >
<div class="cmtMain">
<span class="cmt-god" ></span>

<span class="cmt-name">单眼皮。。…</span>

<div class="main-text">
：还是从前的配方，还是以前的尺寸。
<div class="likenum">
<img src="http://static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad" />


59

</div>
</div>
</div>
</a>



</div>








<div class="article block untagged mb15" id='qiushi_tag_118658311'>

<div class="author clearfix">
<a href="/users/31167196/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/3116/31167196/medium/201701230755037.JPEG" alt="脑补的傻娇啊～"/>
</a>
<a href="/users/31167196/" target="_blank" title="脑补的傻娇啊～">
<h2>脑补的傻娇啊～</h2>
</a>
<div class="articleGender womenIcon">13</div>
</div>



<a href="/article/118658311" target="_blank" class='contentHerf' >
<div class="content">



<span>想到去年的三八妇女节，我给老妈发了祝福信息，我说“妈，三八节日快乐！”<br/>老妈秒回:谢谢，小三八节日同乐……</span>


</div>
</a>





<div class="stats">
<span class="stats-vote"><i class="number">8598</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/118658311" data-share="/article/118658311" id="c-118658311" class="qiushi_comments" target="_blank">
<i class="number">220</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_118658311" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118658311" class="up">
<a href="javascript:voting(118658311,1)" class="voting" data-article="118658311" id="up-118658311" rel="nofollow">
<i></i>
<span class="number hidden">8767</span>
</a>
</li>
<li id="vote-dn-118658311" class="down">
<a href="javascript:voting(118658311,-1)" class="voting" data-article="118658311" id="dn-118658311" rel="nofollow">
<i></i>
<span class="number hidden">-169</span>
</a>
</li>

<li class="comments">
<a href="/article/118658311" id="c-118658311" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>




</div>








<div class="article block untagged mb15" id='qiushi_tag_118661712'>

<div class="author clearfix">
<a href="/users/30936317/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/3093/30936317/medium/201607272359376.JPEG" alt="流星，音晴未雨"/>
</a>
<a href="/users/30936317/" target="_blank" title="流星，音晴未雨">
<h2>流星，音晴未雨</h2>
</a>
<div class="articleGender manIcon">32</div>
</div>



<a href="/article/118661712" target="_blank" class='contentHerf' >
<div class="content">



<span>去老哥家串门没看见读六年级的小侄，老哥说关他在房间里写作业，我就进去看了下，小侄看到我泪汪汪的说：叔，都两个小时了，谢谢你来探监啊，麻烦你救我出去。。    我……</span>


</div>
</a>





<div class="stats">
<span class="stats-vote"><i class="number">7777</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/118661712" data-share="/article/118661712" id="c-118661712" class="qiushi_comments" target="_blank">
<i class="number">48</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_118661712" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118661712" class="up">
<a href="javascript:voting(118661712,1)" class="voting" data-article="118661712" id="up-118661712" rel="nofollow">
<i></i>
<span class="number hidden">7929</span>
</a>
</li>
<li id="vote-dn-118661712" class="down">
<a href="javascript:voting(118661712,-1)" class="voting" data-article="118661712" id="dn-118661712" rel="nofollow">
<i></i>
<span class="number hidden">-152</span>
</a>
</li>

<li class="comments">
<a href="/article/118661712" id="c-118661712" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>




<a href="/article/118661712" class='indexGodCmt' onclick="_hmt.push(['_trackEvent','web_list_god','chick'])" rel="nofollow" target='_blank' >
<div class="cmtMain">
<span class="cmt-god" ></span>

<span class="cmt-name">全国撸管大赛华东分赛总裁判官</span>

<div class="main-text">
：大河向东流啊，谁上神评谁是狗啊！
<div class="likenum">
<img src="http://static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad" />


38

</div>
</div>
</div>
</a>



</div>








<div class="article block untagged mb15" id='qiushi_tag_118665516'>

<div class="author clearfix">
<a href="/users/30996379/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/3099/30996379/medium/20160120204743.jpg" alt="瑞瑞瑞公举"/>
</a>
<a href="/users/30996379/" target="_blank" title="瑞瑞瑞公举">
<h2>瑞瑞瑞公举</h2>
</a>
<div class="articleGender womenIcon">19</div>
</div>



<a href="/article/118665516" target="_blank" class='contentHerf' >
<div class="content">



<span>那说个我大学同学吧，大二晚上八点多去澡堂洗澡，抄小路回宿舍，有个窨井盖被工人掀开忘盖上了，她一脚踩空，但机智如她，居然用手撑住了，向路过的男生呼救，男生看到大晚上窨井里趴着一个披头散发的女子喊救命，吓得头也不回跑走了后来她自己爬上来了</span>


</div>
</a>





<div class="stats">
<span class="stats-vote"><i class="number">4089</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/118665516" data-share="/article/118665516" id="c-118665516" class="qiushi_comments" target="_blank">
<i class="number">98</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_118665516" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118665516" class="up">
<a href="javascript:voting(118665516,1)" class="voting" data-article="118665516" id="up-118665516" rel="nofollow">
<i></i>
<span class="number hidden">4167</span>
</a>
</li>
<li id="vote-dn-118665516" class="down">
<a href="javascript:voting(118665516,-1)" class="voting" data-article="118665516" id="dn-118665516" rel="nofollow">
<i></i>
<span class="number hidden">-78</span>
</a>
</li>

<li class="comments">
<a href="/article/118665516" id="c-118665516" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>




</div>








<div class="article block untagged mb15" id='qiushi_tag_118661029'>

<div class="author clearfix">
<a href="/users/12803665/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/1280/12803665/medium/2016111422311918.JPEG" alt="这个冬天冻成狗"/>
</a>
<a href="/users/12803665/" target="_blank" title="这个冬天冻成狗">
<h2>这个冬天冻成狗</h2>
</a>
<div class="articleGender manIcon">100</div>
</div>



<a href="/article/118661029" target="_blank" class='contentHerf' >
<div class="content">



<span>一哥们最近戒烟了，他是个老烟筒！以前一天近两包烟！<br/><br/>大家问他怎么突然戒烟了，朋友:“我就是想看看，一个不抽烟不喝酒，啥不良爱好都没有的人到底能不能找到女朋友！！！”    这～</span>


</div>
</a>





<div class="stats">
<span class="stats-vote"><i class="number">5970</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/118661029" data-share="/article/118661029" id="c-118661029" class="qiushi_comments" target="_blank">
<i class="number">237</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_118661029" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118661029" class="up">
<a href="javascript:voting(118661029,1)" class="voting" data-article="118661029" id="up-118661029" rel="nofollow">
<i></i>
<span class="number hidden">6090</span>
</a>
</li>
<li id="vote-dn-118661029" class="down">
<a href="javascript:voting(118661029,-1)" class="voting" data-article="118661029" id="dn-118661029" rel="nofollow">
<i></i>
<span class="number hidden">-120</span>
</a>
</li>

<li class="comments">
<a href="/article/118661029" id="c-118661029" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>




</div>








<div class="article block untagged mb15" id='qiushi_tag_118660776'>

<div class="author clearfix">
<span><img src="/static/images/thumb/anony.png?v=b61e7f5162d14b7c0d5f419cd6649c87" alt="匿名用户"/></span>
<span><h2>匿名用户</h2></span>
</div>



<a href="/article/118660776" target="_blank" class='contentHerf' >
<div class="content">



<span>我男朋友逛街时候，　　买了张刮刮乐玩，中了四百。　　他一路开心跑回家，　　跟他妈妈说了，高兴很久后。　　他妈妈说，交出来。。</span>


</div>
</a>





<div class="stats">
<span class="stats-vote"><i class="number">6183</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/118660776" data-share="/article/118660776" id="c-118660776" class="qiushi_comments" target="_blank">
<i class="number">112</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_118660776" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118660776" class="up">
<a href="javascript:voting(118660776,1)" class="voting" data-article="118660776" id="up-118660776" rel="nofollow">
<i></i>
<span class="number hidden">6312</span>
</a>
</li>
<li id="vote-dn-118660776" class="down">
<a href="javascript:voting(118660776,-1)" class="voting" data-article="118660776" id="dn-118660776" rel="nofollow">
<i></i>
<span class="number hidden">-129</span>
</a>
</li>

<li class="comments">
<a href="/article/118660776" id="c-118660776" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>




<a href="/article/118660776" class='indexGodCmt' onclick="_hmt.push(['_trackEvent','web_list_god','chick'])" rel="nofollow" target='_blank' >
<div class="cmtMain">
<span class="cmt-god" ></span>

<span class="cmt-name">飞*常爱你</span>

<div class="main-text">
：一个都谈恋爱了的儿子中了400块钱，老妈都让他交出来，这老妈得扣门成什么样？
<div class="likenum">
<img src="http://static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad" />


12

</div>
</div>
</div>
</a>



</div>








<div class="article block untagged mb15" id='qiushi_tag_118661082'>

<div class="author clearfix">
<a href="/users/30591370/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/3059/30591370/medium/2016112707112448.JPEG" alt="睡觉撞墙卡跟头"/>
</a>
<a href="/users/30591370/" target="_blank" title="睡觉撞墙卡跟头">
<h2>睡觉撞墙卡跟头</h2>
</a>
<div class="articleGender manIcon">29</div>
</div>



<a href="/article/118661082" target="_blank" class='contentHerf' >
<div class="content">



<span>二奶奶在老家院墙外种了一棵樱桃每年都被人偷摘，今年早早就让二爷爷去买一只厉害的狗回来，看谁还敢在偷吃！<br/>结果二爷爷买回来一只吉娃娃，还说说看见这狗太可爱不买都不行。。。</span>


</div>
</a>





<div class="stats">
<span class="stats-vote"><i class="number">6095</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/118661082" data-share="/article/118661082" id="c-118661082" class="qiushi_comments" target="_blank">
<i class="number">84</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_118661082" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118661082" class="up">
<a href="javascript:voting(118661082,1)" class="voting" data-article="118661082" id="up-118661082" rel="nofollow">
<i></i>
<span class="number hidden">6219</span>
</a>
</li>
<li id="vote-dn-118661082" class="down">
<a href="javascript:voting(118661082,-1)" class="voting" data-article="118661082" id="dn-118661082" rel="nofollow">
<i></i>
<span class="number hidden">-124</span>
</a>
</li>

<li class="comments">
<a href="/article/118661082" id="c-118661082" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>




<a href="/article/118661082" class='indexGodCmt' onclick="_hmt.push(['_trackEvent','web_list_god','chick'])" rel="nofollow" target='_blank' >
<div class="cmtMain">
<span class="cmt-god" ></span>

<span class="cmt-name">飞动云懂</span>

<div class="main-text">
：结果第二天，狗也丢了，看见太可爱了，不偷都不行
<div class="likenum">
<img src="http://static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad" />


70

</div>
</div>
</div>
</a>



</div>








<div class="article block untagged mb15" id='qiushi_tag_118653119'>

<div class="author clearfix">
<a href="/users/31381309/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/3138/31381309/medium/2017030218321451.JPEG" alt="姨妈红遍全国"/>
</a>
<a href="/users/31381309/" target="_blank" title="姨妈红遍全国">
<h2>姨妈红遍全国</h2>
</a>
<div class="articleGender womenIcon">12</div>
</div>



<a href="/article/118653119" target="_blank" class='contentHerf' >
<div class="content">



<span>看一个街头恶搞的短片，主持人问一位美女：给你一百块揍你男票一拳，你愿意吗？<br/>只见那男的转身就跑，边跑边喊：她能揍到你破产！！！</span>


</div>
</a>





<div class="stats">
<span class="stats-vote"><i class="number">10657</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/118653119" data-share="/article/118653119" id="c-118653119" class="qiushi_comments" target="_blank">
<i class="number">75</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_118653119" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118653119" class="up">
<a href="javascript:voting(118653119,1)" class="voting" data-article="118653119" id="up-118653119" rel="nofollow">
<i></i>
<span class="number hidden">10881</span>
</a>
</li>
<li id="vote-dn-118653119" class="down">
<a href="javascript:voting(118653119,-1)" class="voting" data-article="118653119" id="dn-118653119" rel="nofollow">
<i></i>
<span class="number hidden">-224</span>
</a>
</li>

<li class="comments">
<a href="/article/118653119" id="c-118653119" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>




<a href="/article/118653119" class='indexGodCmt' onclick="_hmt.push(['_trackEvent','web_list_god','chick'])" rel="nofollow" target='_blank' >
<div class="cmtMain">
<span class="cmt-god" ></span>

<span class="cmt-name">Y彬吖</span>

<div class="main-text">
：主持人:咱俩终于可以在一起了
<div class="likenum">
<img src="http://static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad" />


68

</div>
</div>
</div>
</a>



</div>








<div class="article block untagged mb15" id='qiushi_tag_118657841'>

<div class="author clearfix">
<a href="/users/22615775/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/2261/22615775/medium/20141124112642.jpg" alt="23岁3个孩子"/>
</a>
<a href="/users/22615775/" target="_blank" title="23岁3个孩子">
<h2>23岁3个孩子</h2>
</a>
<div class="articleGender manIcon">23</div>
</div>



<a href="/article/118657841" target="_blank" class='contentHerf' >
<div class="content">



<span>我就是那个二十三岁三个孩子的男人。看这坨也几年了，拉进来的人也不少，发这条说说也不是掘坟贴，我就是想给对门的朋友说一句：“你看下面点的笑脸像不像你欠我的那六百块钱？”</span>


</div>
</a>




<div class="thumb">

<a href="/article/118657841" target="_blank">
<img src="http://pic.qiushibaike.com/system/pictures/11865/118657841/medium/app118657841.jpg" alt="你看下面点的笑脸像不像你欠我的那六百块钱？" />
</a>

</div>



<div class="stats">
<span class="stats-vote"><i class="number">2366</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/118657841" data-share="/article/118657841" id="c-118657841" class="qiushi_comments" target="_blank">
<i class="number">89</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_118657841" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118657841" class="up">
<a href="javascript:voting(118657841,1)" class="voting" data-article="118657841" id="up-118657841" rel="nofollow">
<i></i>
<span class="number hidden">2411</span>
</a>
</li>
<li id="vote-dn-118657841" class="down">
<a href="javascript:voting(118657841,-1)" class="voting" data-article="118657841" id="dn-118657841" rel="nofollow">
<i></i>
<span class="number hidden">-45</span>
</a>
</li>

<li class="comments">
<a href="/article/118657841" id="c-118657841" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>




</div>








<div class="article block untagged mb15" id='qiushi_tag_118664953'>

<div class="author clearfix">
<a href="/users/26723296/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/2672/26723296/medium/20150318143620.jpg" alt="天上掉下个黎妹妹"/>
</a>
<a href="/users/26723296/" target="_blank" title="天上掉下个黎妹妹">
<h2>天上掉下个黎妹妹</h2>
</a>
<div class="articleGender womenIcon">0</div>
</div>



<a href="/article/118664953" target="_blank" class='contentHerf' >
<div class="content">



<span>刚看了个说小时候让人收保护费的，想起小时候我一同学，被小混混拦住要两元钱，我同学说没有零的，只有一张十块的，混混说，没事，我找你八块。然后真找了八块。现在想想，诚信经营啊。</span>


</div>
</a>





<div class="stats">
<span class="stats-vote"><i class="number">2469</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/118664953" data-share="/article/118664953" id="c-118664953" class="qiushi_comments" target="_blank">
<i class="number">31</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_118664953" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118664953" class="up">
<a href="javascript:voting(118664953,1)" class="voting" data-article="118664953" id="up-118664953" rel="nofollow">
<i></i>
<span class="number hidden">2516</span>
</a>
</li>
<li id="vote-dn-118664953" class="down">
<a href="javascript:voting(118664953,-1)" class="voting" data-article="118664953" id="dn-118664953" rel="nofollow">
<i></i>
<span class="number hidden">-47</span>
</a>
</li>

<li class="comments">
<a href="/article/118664953" id="c-118664953" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>




<a href="/article/118664953" class='indexGodCmt' onclick="_hmt.push(['_trackEvent','web_list_god','chick'])" rel="nofollow" target='_blank' >
<div class="cmtMain">
<span class="cmt-god" ></span>

<span class="cmt-name">为了审帖我容易吗</span>

<div class="main-text">
：这种有素质的混混很多最后都成功
<div class="likenum">
<img src="http://static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad" />


26

</div>
</div>
</div>
</a>



</div>








<div class="article block untagged mb15" id='qiushi_tag_118656055'>

<div class="author clearfix">
<a href="/users/33426355/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/3342/33426355/medium/2017021619510077.JPEG" alt="王洋666"/>
</a>
<a href="/users/33426355/" target="_blank" title="王洋666">
<h2>王洋666</h2>
</a>
<div class="articleGender manIcon">27</div>
</div>



<a href="/article/118656055" target="_blank" class='contentHerf' >
<div class="content">



<span>昨天下午领导看到女同事说，你一天不好好上班，换三次衣服，那女同事瞬间恢复，你一天不好好上班老看我换衣服干嘛，领导瞬间涨红了脸…</span>


</div>
</a>





<div class="stats">
<span class="stats-vote"><i class="number">6258</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/118656055" data-share="/article/118656055" id="c-118656055" class="qiushi_comments" target="_blank">
<i class="number">58</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_118656055" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118656055" class="up">
<a href="javascript:voting(118656055,1)" class="voting" data-article="118656055" id="up-118656055" rel="nofollow">
<i></i>
<span class="number hidden">6385</span>
</a>
</li>
<li id="vote-dn-118656055" class="down">
<a href="javascript:voting(118656055,-1)" class="voting" data-article="118656055" id="dn-118656055" rel="nofollow">
<i></i>
<span class="number hidden">-127</span>
</a>
</li>

<li class="comments">
<a href="/article/118656055" id="c-118656055" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>




<a href="/article/118656055" class='indexGodCmt' onclick="_hmt.push(['_trackEvent','web_list_god','chick'])" rel="nofollow" target='_blank' >
<div class="cmtMain">
<span class="cmt-god" ></span>

<span class="cmt-name">kkkkk~</span>

<div class="main-text">
：天生妙物腿间居， 雅称玉户俗称逼， 茸茸美髯红唇隐， 幽幽深谷甘露滴， 无牙偏爱吃硬肉， 嘴小却喜吞大鸡， 最是令人销魂处， 亦收亦缩亦吮吸
<div class="likenum">
<img src="http://static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad" />


35

</div>
</div>
</div>
</a>



</div>








<div class="article block untagged mb15" id='qiushi_tag_118650164'>

<div class="author clearfix">
<a href="/users/29314260/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/2931/29314260/medium/20170226112657.JPEG" alt="(糗名昭著)~贝贝"/>
</a>
<a href="/users/29314260/" target="_blank" title="(糗名昭著)~贝贝">
<h2>(糗名昭著)~贝贝</h2>
</a>
<div class="articleGender womenIcon">26</div>
</div>



<a href="/article/118650164" target="_blank" class='contentHerf' >
<div class="content">



<span>小侄女在幼儿园老是跟小盆友打 架，被老师停 课一星期！<br/>每每别人问她:妞妞，今天咋又没上幼儿园呀？小侄女都会笑嘻嘻的说:老师说我表现好，奖 励我休 假一星期！<br/><br/>艾玛...你脸皮这么厚随谁呀</span>


</div>
</a>





<div class="stats">
<span class="stats-vote"><i class="number">6801</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/118650164" data-share="/article/118650164" id="c-118650164" class="qiushi_comments" target="_blank">
<i class="number">226</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_118650164" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118650164" class="up">
<a href="javascript:voting(118650164,1)" class="voting" data-article="118650164" id="up-118650164" rel="nofollow">
<i></i>
<span class="number hidden">6947</span>
</a>
</li>
<li id="vote-dn-118650164" class="down">
<a href="javascript:voting(118650164,-1)" class="voting" data-article="118650164" id="dn-118650164" rel="nofollow">
<i></i>
<span class="number hidden">-146</span>
</a>
</li>

<li class="comments">
<a href="/article/118650164" id="c-118650164" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>




</div>








<div class="article block untagged mb15" id='qiushi_tag_118655382'>

<div class="author clearfix">
<a href="/users/6193692/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/619/6193692/medium/2016111002403187.JPEG" alt="小温侯★瀧羊"/>
</a>
<a href="/users/6193692/" target="_blank" title="小温侯★瀧羊">
<h2>小温侯★瀧羊</h2>
</a>
<div class="articleGender manIcon">21</div>
</div>



<a href="/article/118655382" target="_blank" class='contentHerf' >
<div class="content">



<span>感觉好累，发了个动态：来世真想变成一只狗狗，饿了就吃，吃了就睡，一看到街上的小母狗上去就……<br/>朋友秒回：想吃屎就直接说，别这么拐弯抹角……</span>


</div>
</a>





<div class="stats">
<span class="stats-vote"><i class="number">8859</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/118655382" data-share="/article/118655382" id="c-118655382" class="qiushi_comments" target="_blank">
<i class="number">155</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_118655382" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118655382" class="up">
<a href="javascript:voting(118655382,1)" class="voting" data-article="118655382" id="up-118655382" rel="nofollow">
<i></i>
<span class="number hidden">9059</span>
</a>
</li>
<li id="vote-dn-118655382" class="down">
<a href="javascript:voting(118655382,-1)" class="voting" data-article="118655382" id="dn-118655382" rel="nofollow">
<i></i>
<span class="number hidden">-200</span>
</a>
</li>

<li class="comments">
<a href="/article/118655382" id="c-118655382" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>




</div>







<ul class="pagination">


<li>
<span class="current" >
1
</span>
</li>




<li>
<a href="/hot/page/2?s=4962602" rel="nofollow">
<!--<a href="/hot/page/2/" rel="nofollow">-->
<span class="page-numbers">
2
</span>
</a>
</li>



<li>
<a href="/hot/page/3?s=4962602" rel="nofollow">
<!--<a href="/hot/page/3/" rel="nofollow">-->
<span class="page-numbers">
3
</span>
</a>
</li>



<li>
<a href="/hot/page/4?s=4962602" rel="nofollow">
<!--<a href="/hot/page/4/" rel="nofollow">-->
<span class="page-numbers">
4
</span>
</a>
</li>



<li>
<a href="/hot/page/5?s=4962602" rel="nofollow">
<!--<a href="/hot/page/5/" rel="nofollow">-->
<span class="page-numbers">
5
</span>
</a>
</li>



<li>
<span class="dots">
…
</span>
</li>


<li>
<a href="/hot/page/35?s=4962602" rel="nofollow">
<!--<a href="/hot/page/35/" rel="nofollow">-->
<span class="page-numbers">
35
</span>
</a>
</li>


<li>
<a href="/hot/page/2?s=4962602" rel="nofollow">
<!--<a href="/hot/page/2/" rel="nofollow">-->
<span class="next">
下一页
</span>
</a>
</li>

</ul>

</div>


<div class="col2">
<div id="sidebar" class="sidebar">
<div class="shopwindow">
<!-- 55736471：web-右侧固定-up 类型：固定 尺寸：300x250-->
<script type="text/javascript">//<![CDATA[
ac_as_id = "mm_108378320_13540554_55736471";
ac_format = 1;
ac_mode = 1;
ac_group_id = 1;
ac_server_base_url = "afpeng.alimama.com/";
//]]></script>
<script type="text/javascript" src="http://afpmm.alicdn.com/g/mm/afp-cdn/JS/k.js"></script>
</div>
<div class="shopwindow">
<!-- 55736474：web-右侧固定-dn 类型：固定 尺寸：300x250-->
<script type="text/javascript">//<![CDATA[
ac_as_id = "mm_108378320_13540554_55736474";
ac_format = 1;
ac_mode = 1;
ac_group_id = 1;
ac_server_base_url = "afpeng.alimama.com/";
//]]></script>
<script type="text/javascript" src="http://afpmm.alicdn.com/g/mm/afp-cdn/JS/k.js"></script>
</div>


<div class="sidebar-tutorial clearfix">
<h3>糗百小提示</h3>
<div class="sidebar-tutorial-block">
<div class="sidebar-tutorial-keyboard"></div>
<div class="sidebar-tutorial-text">按 Ctrl+D 键，把糗事百科加入收藏夹</div>
</div>
</div>
<div class="sidebar-hot clearfix">
<h3>爆笑糗事精选</h3>
<ul>

<li class="item">
<a href="/article/118498138" rel="nofollow">
<span><img src="http://pic.qiushibaike.com/system/pictures/11849/118498138/medium/app118498138.jpg?imageView2/1/w/146/h/146" alt="每个妈妈都会告诉自己的女儿保护好自己"/></span>
</a>
<a href="/article/118498138" title="每个妈妈都会告诉自己的女儿保护好自己" rel="nofollow">
<p>每个妈妈都会告诉自己的女儿保护好自己</p>
</a>
</li>

<li class="item">
<a href="/article/118611680" rel="nofollow">
<span><img src="http://pic.qiushibaike.com/system/pictures/11861/118611680/medium/app118611680.jpg?imageView2/1/w/146/h/146" alt="非要五个字，，"/></span>
</a>
<a href="/article/118611680" title="非要五个字，，" rel="nofollow">
<p>非要五个字，，</p>
</a>
</li>

<li class="item">
<a href="/article/118543105" rel="nofollow">
<span><img src="http://pic.qiushibaike.com/system/pictures/11854/118543105/medium/app118543105.jpg?imageView2/1/w/146/h/146" alt="这是最后一次了"/></span>
</a>
<a href="/article/118543105" title="这是最后一次了" rel="nofollow">
<p>这是最后一次了</p>
</a>
</li>

<li class="item">
<a href="/article/118522689" rel="nofollow">
<span><img src="http://pic.qiushibaike.com/system/pictures/11852/118522689/medium/app118522689.jpg?imageView2/1/w/146/h/146" alt="坐等二楼和十四楼的巧遇"/></span>
</a>
<a href="/article/118522689" title="坐等二楼和十四楼的巧遇" rel="nofollow">
<p>坐等二楼和十四楼的巧遇</p>
</a>
</li>

<li class="item">
<a href="/article/118611315" rel="nofollow">
<span><img src="http://pic.qiushibaike.com/system/pictures/11861/118611315/medium/app118611315.jpg?imageView2/1/w/146/h/146" alt="但是我一直不想用"/></span>
</a>
<a href="/article/118611315" title="但是我一直不想用" rel="nofollow">
<p>但是我一直不想用</p>
</a>
</li>

<li class="item">
<a href="/article/118533498" rel="nofollow">
<span><img src="http://pic.qiushibaike.com/system/pictures/11853/118533498/medium/app118533498.jpg?imageView2/1/w/146/h/146" alt="成语填词"/></span>
</a>
<a href="/article/118533498" title="成语填词" rel="nofollow">
<p>成语填词</p>
</a>
</li>

<li class="item">
<a href="/article/118536295" rel="nofollow">
<span><img src="http://pic.qiushibaike.com/system/pictures/11853/118536295/medium/app118536295.jpg?imageView2/1/w/146/h/146" alt="以为牢不可破的关系"/></span>
</a>
<a href="/article/118536295" title="以为牢不可破的关系" rel="nofollow">
<p>以为牢不可破的关系</p>
</a>
</li>

<li class="item">
<a href="/article/118616244" rel="nofollow">
<span><img src="http://pic.qiushibaike.com/system/pictures/11861/118616244/medium/app118616244.jpg?imageView2/1/w/146/h/146" alt="哈哈哈"/></span>
</a>
<a href="/article/118616244" title="哈哈哈" rel="nofollow">
<p>哈哈哈</p>
</a>
</li>

</ul>
</div>
<div class="sidebar-hot clearfix">
<h3>热门话题<a class="more" href="/joke/">更多 ></a></h3>
<div class="sidebar-tag-block">


<li><i># </i><a href="/joke/44505/">217年春节放假安排</a><i> #</i></li>

<li><i># </i><a href="/joke/39706/">霸气搞笑点的开黑id</a><i> #</i></li>

<li><i># </i><a href="/joke/29617/">群主搞笑打油诗</a><i> #</i></li>

<li><i># </i><a href="/joke/29367/">你比我猜搞笑题目</a><i> #</i></li>

<li><i># </i><a href="/joke/22899/">新闻联播搞笑开场白</a><i> #</i></li>

<li><i># </i><a href="/joke/18777/">微信搞笑视频群</a><i> #</i></li>

<li><i># </i><a href="/joke/14610/">数学小笑话20字</a><i> #</i></li>

<li><i># </i><a href="/joke/12727/">分享几个经典的逗女孩子开心的笑话</a><i> #</i></li>

<li><i># </i><a href="/joke/11935/">开心一刻幽默小笑话带图片</a><i> #</i></li>

<li><i># </i><a href="/joke/10545/">起床了搞笑图片表情</a><i> #</i></li>

<li><i># </i><a href="/joke/9386/">多玩搞笑gif</a><i> #</i></li>

<li><i># </i><a href="/joke/9097/">群聊搞笑图片笑死人</a><i> #</i></li>

<li><i># </i><a href="/joke/4938/">当代雷锋人物有哪些</a><i> #</i></li>

<li><i># </i><a href="/joke/4287/">小学生幽默小品剧本</a><i> #</i></li>

<li><i># </i><a href="/joke/2745/">过年租车</a><i> #</i></li>

<li><i># </i><a href="/joke/1280/">元宵情人节</a><i> #</i></li>

<li><i># </i><a href="/joke/388/">小学生组词笑话</a><i> #</i></li>

<li><i># </i><a href="/joke/352/">小学生搞笑作文老师评语</a><i> #</i></li>

<li><i># </i><a href="/joke/300/">情侣之间的搞笑称呼</a><i> #</i></li>

<li><i># </i><a href="/joke/201/">骂人图片带字搞笑图片</a><i> #</i></li>


</div>
</div>


<div class="shopwindow">
<!-- 55736473：web-右侧悬浮-up 类型：固定 尺寸：300x250-->
<script type="text/javascript">//<![CDATA[
ac_as_id = "mm_108378320_13540554_55736473";
ac_format = 1;
ac_mode = 1;
ac_group_id = 1;
ac_server_base_url = "afpeng.alimama.com/";
//]]></script>
<script type="text/javascript" src="http://afpmm.alicdn.com/g/mm/afp-cdn/JS/k.js"></script>
</div>

<div class="shopwindow">
<!-- 55736475：web-右侧悬浮-dn 类型：固定 尺寸：300x250-->
<script type="text/javascript">//<![CDATA[
ac_as_id = "mm_108378320_13540554_55736475";
ac_format = 1;
ac_mode = 1;
ac_group_id = 1;
ac_server_base_url = "afpeng.alimama.com/";
//]]></script>
<script type="text/javascript" src="http://afpmm.alicdn.com/g/mm/afp-cdn/JS/k.js"></script>
</div>

</div>
</div>



</div>
</div>


<div class="foot">
 <div class="foot-ad">
<!--<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>-->
<!--&lt;!&ndash; 16-糗事百科首页底部_BTF_728x90 &ndash;&gt;-->
<!--<ins class="adsbygoogle"-->
<!--style="display:inline-block;width:728px;height:90px"-->
<!--data-ad-client="ca-pub-4939841000086153"-->
<!--data-ad-slot="5196507409"></ins>-->
<!--<script>-->
<!--(adsbygoogle = window.adsbygoogle || []).push({});-->
<!--</script>-->
<!-- 68902435：web-底部固定 类型：固定 尺寸：728x90-->
<script type="text/javascript">//<![CDATA[
ac_as_id = "mm_108378320_13540554_68902435";
ac_format = 1;
ac_mode = 1;
ac_group_id = 1;
ac_server_base_url = "afpeng.alimama.com/";
//]]></script>
<script type="text/javascript" src="http://afpmm.alicdn.com/g/mm/afp-cdn/JS/k.js"></script>
</div>

<div class="foot-nav clearfix">
<div class="foot-nav-col">
<h3>
关于
</h3>
<ul>
<li>
<a href="http://about.qiushibaike.com/web_jobs.html#team" target="_blank" rel="nofollow">
关于糗百
</a>
</li>
<li>
<a href="http://about.qiushibaike.com/web_jobs.html#tech" target="_blank" rel="nofollow">
加入我们
</a>
</li>
<li>
<a href="http://about.qiushibaike.com/web_jobs.html#contact" target="_blank" rel="nofollow">
联系方式
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
帮助
</h3>
<ul>
<li>
<a href="http://about.qiushibaike.com/feedback.html" target="_blank" rel="nofollow">
在线反馈
</a>
</li>
<li>
<a href="http://about.qiushibaike.com/agreement.html" target="_blank" rel="nofollow">
用户协议
</a>
</li>
<li>
<a href="http://about.qiushibaike.com/policy.html" target="_blank" rel="nofollow">
隐私政策
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
下载
</h3>
<ul>
<li>
<a href="http://android.myapp.com/android/appdetail.jsp?appid=107431&icfa=15144196000105020000&lmid=2031"
target="_blank" rel="external nofollow">
Android 客户端
</a>
</li>
<li>
<a href="http://itunes.apple.com/app/id422853458" target="_blank" rel="external nofollow">
iPhone 客户端
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
关注
</h3>
<ul>
<li>
<a href="#" class="foot-wechat">
微信
<div class="foot-wechat-tips">
<span class="foot-wechat-icon"></span>
手机扫描二维码关注
</div>
</a>
</li>
<li>
<a href="http://weibo.com/qiushibaike" target="_blank" rel="external nofollow">
新浪微博
</a>
</li>
<li>
<a href="http://user.qzone.qq.com/1492495058" target="_blank" rel="external nofollow">
QQ空间
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
组织
</h3>
<ul>
<li>
<a href="http://shang.qq.com/wpa/qunwpa?idkey=da34d190ca97a0b21d64ebc6f3ab72c076ed35820e629b78fcf9f6a78f7063cd"
target="_blank" rel="external nofollow">
网站反馈群
</a>
</li>
<li>
<a href="http://user.qzone.qq.com/1492495058/blog/1408597608" target="_blank"
rel="external nofollow">
官方粉丝群
</a>
</li>
</ul>
</div>
</div>
<div class="foot-copyrights">
<p>&copy; Qiushibaike.com 糗事百科版权所有</p>
<p>
<span>京ICP备14028348号-1</span>
<span>京ICP证140448号</span>
<span>
<a style='color:#333' target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502031601" rel="nofollow"><img style='vertical-align: top;' src="/static/images/beian.png?v=d0289dc0a46fc5b15b3363ffa78cf6c7" />京公网安备11010502031601号</a>
</span>
</p>
<p style="margin-top:8px">友际无限（北京）科技有限公司</p>
<p style="margin-top:8px">
<span>互联网违法和不良信息举报电话：010-84872896</span>
<span>邮箱：kefu@qiushibaike.com</span>
</p>
</div>
</div>


<div class="signin-box" id="login-form">
<div class="sigin-left">
<div class="signin-account clearfix">
<h4 class="social-signin-heading">社交帐号登录</h4>
<a rel="external nofollow" oauth_href href="https://open.weixin.qq.com/connect/qrconnect?appid=wx559af2d26b56c655&redirect_uri=http%3A%2F%2Fwww.qiushibaike.com%2Fnew4%2Fsession%3Fsrc%3Dwx&response_type=code&scope=snsapi_login#wechat_redirect" class="social-btn social-wechat">
使用 微信 账号</a>
<a rel="external nofollow" oauth_href href="https://api.weibo.com/oauth2/authorize?client_id=63372306&redirect_uri=http%3A%2F%2Fwww.qiushibaike.com%2Fnew4%2Fsession" class="social-btn social-weibo">
使用 微博 账号</a>
<a rel="external nofollow" oauth_href href="https://graph.qq.com/oauth2.0/authorize?which=Login&display=pc&client_id=100251437&response_type=code&redirect_uri=www.qiushibaike.com/new4/session?src=qq" class="social-btn social-qq">
使用 QQ 账号 </a>
</div>
<div class="signin-form clearfix">
<h4 class="social-signin-heading">糗事百科账号登录</h4>
<form method="post" action="/new4/session">
<input type="hidden" name="_xsrf" value="2|df20512d|181c91d239d25ebcb0985a6ecea25a31|1488780601"/>
<div class="signin-section clearfix">
<input type="text" class="form-input form-input-first" name="login" placeholder="昵称或邮箱">
<input type="password" class="form-input" name="password" placeholder="密码">
<input type="checkbox" id="remember_me" name="remember_me" checked="" value="checked" style="display:none">
</div>
<div class="signin-error" id="signin-error"></div>
<button type="submit" id="form-submit" class="form-submit">登录</button>
</form>
</div>
<div class="signin-foot clearfix">
<a rel="nofollow" href="/new4/fetchpass" class="fetch-password">忘记密码?</a>
</div>
</div>
</div>

<div class="float-nav">
<a class="float-nav-backtop" href="#" rel="nofollow">
<span class="float-nav-backtop-icon"></span>
</a>
</div>

<!--[if gte IE 6]>
<script type="text/javascript" src="http://static.qiushibaike.com/js/src/web/json3.js?v=3a7f66a11a09842cd7555fad039657be"></script>
<![endif]-->
<script type="text/javascript" src="http://static.qiushibaike.com/js/dist/web/libs.min.js?v=bc8ddd36f0e7fed7c27f437c17f23ce0"></script>
<script type="text/javascript" src="http://static.qiushibaike.com/js/dist/web/app.min.js?v=9d24424ee8d18d35a0a64362f6e6694a"></script>



<script type="text/javascript">
// Google Analytics
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-8780108-1', 'auto');
ga('send', 'pageview');
</script>
</body>
</html>

http://www.qiushibaike.com/hot/page/1

Process finished with exit code 0
'''
