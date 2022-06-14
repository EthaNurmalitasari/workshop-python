import pandas as pd

path = "songs_normalize.csv"
df = pd.read_csv(path)

df.head()
#output
artist	song	duration_ms	explicit	year	popularity	danceability	energy	key	loudness	mode	speechiness	acousticness	instrumentalness	liveness	valence	tempo	genre
0	Britney Spears	Oops!...I Did It Again	211160	False	2000	77	0.751	0.834	1	-5.444	0	0.0437	0.3000	0.000018	0.3550	0.894	95.053	pop
1	blink-182	All The Small Things	167066	False	1999	79	0.434	0.897	0	-4.918	1	0.0488	0.0103	0.000000	0.6120	0.684	148.726	rock, pop
2	Faith Hill	Breathe	250546	False	1999	66	0.529	0.496	7	-9.007	1	0.0290	0.1730	0.000000	0.2510	0.278	136.859	pop, country
3	Bon Jovi	It's My Life	224493	False	2000	78	0.551	0.913	0	-4.063	0	0.0466	0.0263	0.000013	0.3470	0.544	119.992	rock, metal
4	*NSYNC	Bye Bye Bye	200560	False	2000	65	0.614	0.928	8	-4.806	0	0.0516	0.0408	0.001040	0.0845	0.879	172.656	pop

df.tail()
#output
artist	song	duration_ms	explicit	year	popularity	danceability	energy	key	loudness	mode	speechiness	acousticness	instrumentalness	liveness	valence	tempo	genre
1995	Jonas Brothers	Sucker	181026	False	2019	79	0.842	0.734	1	-5.065	0	0.0588	0.0427	0.000000	0.1060	0.952	137.958	pop
1996	Taylor Swift	Cruel Summer	178426	False	2019	78	0.552	0.702	9	-5.707	1	0.1570	0.1170	0.000021	0.1050	0.564	169.994	pop
1997	Blanco Brown	The Git Up	200593	False	2019	69	0.847	0.678	9	-8.635	1	0.1090	0.0669	0.000000	0.2740	0.811	97.984	hip hop, country
1998	Sam Smith	Dancing With A Stranger (with Normani)	171029	False	2019	75	0.741	0.520	8	-7.513	1	0.0656	0.4500	0.000002	0.2220	0.347	102.998	pop
1999	Post Malone	Circles	215280	False	2019	85	0.695	0.762	0	-3.497	1	0.0395	0.1920	0.002440	0.0863	0.553	120.042	hip hop

df.info()
#output
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2000 entries, 0 to 1999
Data columns (total 18 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   artist            2000 non-null   object 
 1   song              2000 non-null   object 
 2   duration_ms       2000 non-null   int64  
 3   explicit          2000 non-null   bool   
 4   year              2000 non-null   int64  
 5   popularity        2000 non-null   int64  
 6   danceability      2000 non-null   float64
 7   energy            2000 non-null   float64
 8   key               2000 non-null   int64  
 9   loudness          2000 non-null   float64
 10  mode              2000 non-null   int64  
 11  speechiness       2000 non-null   float64
 12  acousticness      2000 non-null   float64
 13  instrumentalness  2000 non-null   float64
 14  liveness          2000 non-null   float64
 15  valence           2000 non-null   float64
 16  tempo             2000 non-null   float64
 17  genre             2000 non-null   object 
dtypes: bool(1), float64(9), int64(5), object(3)
memory usage: 267.7+ KB


df.tail(3)
#output
artist	song	duration_ms	explicit	year	popularity	danceability	energy	key	loudness	mode	speechiness	acousticness	instrumentalness	liveness	valence	tempo	genre
1997	Blanco Brown	The Git Up	200593	False	2019	69	0.847	0.678	9	-8.635	1	0.1090	0.0669	0.000000	0.2740	0.811	97.984	hip hop, country
1998	Sam Smith	Dancing With A Stranger (with Normani)	171029	False	2019	75	0.741	0.520	8	-7.513	1	0.0656	0.4500	0.000002	0.2220	0.347	102.998	pop
1999	Post Malone	Circles	215280	False	2019	85	0.695	0.762	0	-3.497	1	0.0395	0.1920	0.002440	0.0863	0.553	120.042	hip hop


df.sample(5)
#output
artist	song	duration_ms	explicit	year	popularity	danceability	energy	key	loudness	mode	speechiness	acousticness	instrumentalness	liveness	valence	tempo	genre
1591	BØRNS	Electric Love	218173	False	2015	0	0.373	0.858	6	-6.536	0	0.0889	0.00407	0.001600	0.2560	0.605	120.063	rock, pop
1685	Sia	The Greatest (feat. Kendrick Lamar)	210226	False	2016	68	0.668	0.725	1	-6.127	1	0.2660	0.01020	0.000479	0.0561	0.729	191.944	pop
1129	LMFAO	Sexy And I Know It	199480	False	2011	67	0.707	0.861	7	-4.225	1	0.3160	0.10000	0.000000	0.1910	0.795	130.021	hip hop, pop, Dance/Electronic
470	Avril Lavigne	Don't Tell Me	202013	False	2004	58	0.523	0.795	4	-2.920	1	0.0386	0.00462	0.000000	0.3580	0.484	144.106	pop
846	Natasha Bedingfield	Pocketful of Sunshine	203440	False	2008	62	0.726	0.881	9	-3.892	0	0.0391	0.20300	0.000000	0.1080	0.682	110.019	pop


df.loc[0:3, ['artist', 'song']]
#output
	artist	song
0	Britney Spears	Oops!...I Did It Again
1	blink-182	All The Small Things
2	Faith Hill	Breathe
3	Bon Jovi	It's My Life


df.loc[0:3, ['artist', 'song', 'year']]
df.iloc[0:3, [0, 1, 3]]
df[['artist', 'song', 'year']][:3]
df[:3][['artist', 'song', 'year']]
#output
artist	song	year
0	Britney Spears	Oops!...I Did It Again	2000
1	blink-182	All The Small Things	1999
2	Faith Hill	Breathe	1999