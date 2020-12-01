# Majhong (15112 Project)

### Description:

There are 4 players in total, banker will start first will have 14 tiles, other 3 players will have 13 tiles. The user is able to play with 3 AI.

There are (9*3+7) *4 tiles in total and they have the following category.

##### 万 (Wan) (Sequence)

<img src="pic/tile_type3_300ppi/3-1.png" alt="avatar" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-2.png" alt="avatar" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-3.png" alt="avatar" width="65" height="80"/><img src="pic/tile_type3_300ppi/3-4.png" alt="avatar" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-5.png" alt="avatar" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-6.png" alt="avatar" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-7.png" alt="avatar" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-8.png" alt="avatar" width="65" height="80"  /><img src="pic/tile_type3_300ppi/3-9.png" alt="avatar" width="65" height="80" />

##### 筒 (Tong) (Sequence)

<img src="pic/tile_type3_300ppi/3-10.png" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-11.png" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-12.png" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-13.png" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-14.png" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-15.png" alt="avatar" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-16.png" alt="avatar" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-17.png" alt="avatar" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-18.png" alt="avatar" width="65" height="80" />

##### 条 (Tiao) (Sequence)

<img src="pic/tile_type3_300ppi/3-19.png" alt="avatar" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-20.png" alt="avatar" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-21.png" alt="avatar" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-22.png" alt="avatar" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-23.png" alt="avatar" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-24.png" alt="avatar" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-25.png" alt="avatar" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-26.png" alt="avatar" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-27.png" alt="avatar" width="65" height="80" />

##### 风 (Feng)

<img src="pic/tile_type3_300ppi/3-28.png" alt="avatar" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-29.png" alt="avatar" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-30.png" alt="avatar" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-31.png" alt="avatar" width="65" height="80" />

##### 白板，发财，红中 (Other tiles)

<img src="pic/tile_type3_300ppi/3-32.png" alt="avatar" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-33.png" alt="avatar" width="65" height="80" /><img src="pic/tile_type3_300ppi/3-34.png" alt="avatar" width="65" height="80" />



Each round, player will have to draw a tile and discard a card. 

In the middle of the game, people can have 2 special action: Peng 碰/Gang杠

##### Peng Action (碰): 

If player A discarded a tile, which Player B have 2 same tiles. Player B can take the Peng action and have all three tiles into the action tiles stack. And the game will enter player B round. Player B will discard a tile.

##### Gang Action (杠): 

Type1

If player A discarded a tile, which Player B have 3 same tiles. Player B can take the Gang action and have all four tiles into the action tiles stack. And the game will enter player B round. Player B will draw a tile first and then discard a tile.

Type 2

If player A in his round has 4 same tiles, he can use the Gang action to take all four tiles into the action tiles stack. He will draw a tile and discard a tile.

##### Hu (胡) (Winning): 

The first person reaches the combination of AA+nBBB+nCDE or AABBCCDDEEFFGG 7 pairs will win the game! Different combination of tiles will decide the points which the winner wins.



### Library requirement:

Required library: python(3.8), pygame

### How to run the game

In order to run the game, please clone all the packages to your local directory and run the screen.py file to run the whole game! 

REMEMBER to download the pic folder and sound folder, otherwise the game will not run with pictures and sound effects!!!

### Game Live Images

##### Demo1

![PlayDemo1](pic/PlayDemo1.png)



##### Demo2

##### ![PlayDemo2](pic/PlayDemo2.png)



##### Demo3

##### ![PlayDemo3](pic/PlayDemo3.png)



##### Lost page

##### ![LostPageDemo](pic/LostPageDemo.png)



##### Win Page

![WinPageDemo](pic/WinPageDemo.png)







