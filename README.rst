for-lossless-music
===================

|PyPI version|

创建这个项目是觉得每次找无损音乐太烦了， 还浪费时间，
开了个QQ绿钻， 结果有一些歌曲下载的还是加密格式。

feature
-------
- 可以搜索
- 可以下载
- 可以根据QQ加密格式目录下载相同歌名
- 可以自动根据歌手名分文件存储
- 加入pypi

install
-------
::

   pip3 install for-lossless-music


usage example
^^^^^^^^^^^^^
::

   for-lossless-music 人质 #搜索歌曲人质
   for-lossless-music 人质 -i 1 -o ~/Downloads #下载搜索人质id=1的歌曲到～/Downloads目录
   for-lossless-music 人质 -i 1 -o ~/Downloads -c # 同上但是会下载到自动创建歌手文件夹中


plan
----
预期从 http://moresound.tk 下载， 此网站是可以手动下载的，
但是手动搜索下载多了以后发现一个问题，是下载之后的文件名问题，
所以想用脚本改进一下。


TODO
^^^^
- 可以根据一定的规则来过滤搜索
- 同时搜索几个来源，合并成一起显示
- 搜索后并不退出，可以不断的搜索并下载
- 可以从歌单下载歌曲（预计先支持QQ， 后期加入网易）

image
-----
搜索

.. image:: https://user-images.githubusercontent.com/19854253/46993569-78d3e700-d142-11e8-9569-99e48fe5b322.png

下载

.. image:: https://user-images.githubusercontent.com/19854253/47006312-33c2ab80-d168-11e8-848d-eecb7a217911.png

自动根据目录下载

.. image:: https://user-images.githubusercontent.com/19854253/47007342-93ba5180-d16a-11e8-9bea-4e719a3ca453.gif


.. |PyPI version| image:: https://img.shields.io/pypi/v/for-lossless-music.svg
   :target: https://pypi.org/project/for-lossless-music/
