import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  @ViewChild('videoPlayer') videoPlayer: ElementRef;
  title = 'userstudy';

  // if true, we are currently conducting a page load test
  spacebarPressed = false;

  // list of videos
  videos = [
    'video1.mp4',
    'video2.mp4',
    'video3.mp4',
    'video4.mp4',
    'video5.mp4',
    'video6.mp4',
  ];

  results = [];

  // current video index
  index = 0;

  resultsIndex = 0;

  startTime = -1;

  finished = false;

  ngOnInit(): void {
    const context = this;
    document.body.onkeyup = (e) => {
      if (!context.finished && (e.keyCode === 32 || e.key === ' ')) {
        console.log(this.index % 3)
        if (this.index % 3 === 0) {
          context.showDemoVideo(context);
        } else {
          context.recordNextVideo(context);
        }
      }
    };
  }

  showDemoVideo(context): void {
    if (context.spacebarPressed) {
      context.spacebarPressed = false;
      context.stopVideo();
      context.index++;
    } else {
      context.spacebarPressed = true;
      context.playVideo();
    }

  }

  recordNextVideo(context): void {
    if (context.spacebarPressed) {
      context.spacebarPressed = false;
      context.results[context.resultsIndex] = performance.now() - context.startTime;
      context.stopVideo();
      if ((context.resultsIndex + 1) === context.videos.length) {
        context.finish(context);
        console.log(context.results);
      } else {
        context.index++;
        context.resultsIndex++;
      }
    } else {
      context.spacebarPressed = true;
      context.startTime = performance.now();
      context.playVideo();
    }
  }

  finish(context): void {
    context.finished = true;
  }


  playVideo(): void {
    this.videoPlayer.nativeElement.load();
    this.videoPlayer.nativeElement.play();
  }

  stopVideo(): void {
    this.videoPlayer.nativeElement.pause();
  }

  round(amount): number {
    return Math.round(amount * 100) / 100;
  }
}
