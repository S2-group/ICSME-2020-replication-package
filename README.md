# Measuring metrics

Go to the root of the repo. Create the folder `results`.

Go to `metrics`. Install the dependencies via NPM:

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
node main.js --url https://google.com --file myresult.csv --runs 30
```
