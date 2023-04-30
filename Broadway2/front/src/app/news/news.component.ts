import { Component } from '@angular/core';
import { News } from '../models';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-news',
  templateUrl: './news.component.html',
  styleUrls: ['./news.component.css']
})
export class NewsComponent {
  main_news_list: News[] = []
  constructor(private apiService: ApiService){

  }

  ngOnInit(){
    this.getMainNews();
  }



  getMainNews = () => {
    this.apiService.getMainNews().subscribe(
      data => {
        this.main_news_list = data;
      },
      error => {
        console.log(error);
      }
    )
  }
}
