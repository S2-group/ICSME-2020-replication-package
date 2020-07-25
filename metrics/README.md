# Measuring metrics
Install the dependencies via `npm install`, or manually:

```
npm install lighthouse
npm install minimist
npm install fs
npm install chrome-har-capturer
npm install percentile
```

Also install lighthouse globally:
```
npm install lighthouse
```
Now launch chrome-debug in the background using the start-chrome.bat or start-chrome.sh script.

Now run the script:

```
npm start -- --url https://google.com --file myresult.csv --folder somefolder --runs 30
```
