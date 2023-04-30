import { Component } from '@angular/core';
import {Club, News} from "../models";
import {ApiService} from "../api.service";

@Component({
  selector: 'app-news-list',
  templateUrl: './news-list.component.html',
  styleUrls: ['./news-list.component.css']
})
export class NewsListComponent {
  news_list: News[] = []
  constructor(private api: ApiService) {
  }
  ngOnInit(){
    this.getAllClubs();
  }

  getAllClubs(){
    this.api.getAllNews().subscribe((data) => {
      this.news_list = data;
    } )
  }
}
