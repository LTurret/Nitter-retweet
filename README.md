# nitter-retweet

A tool for debug some twitter features in [ArisaMatsuda](https://github.com/LTurret/ArisaMatsuda)

## Related functions

- [fetch_tweet.py](https://github.com/LTurret/ArisaMatsuda/blob/main/cogs/src/fetch_tweet.py)
- [get_contents.py](https://github.com/LTurret/ArisaMatsuda/blob/main/cogs/src/get_contents.py)
- [get_tokens.py](https://github.com/LTurret/ArisaMatsuda/blob/main/cogs/src/get_tokens.py)

## Build

### Requirements

```plain
aiohttp==3.8.5
aiosignal==1.3.1
async-timeout==4.0.3
attrs==23.1.0
beautifulsoup4==4.12.2
charset-normalizer==3.2.0
frozenlist==1.4.0
idna==3.4
multidict==6.0.4
soupsieve==2.5
tqdm==4.66.1
yarl==1.9.2
```

### Running

```shell
python3 -B main.py
```

> [!NOTE]
> The `-B` prevents `__pycache__` being created

### Output

`/test` will created after program finish

## License

Licensed under [MIT](LICENSE).
