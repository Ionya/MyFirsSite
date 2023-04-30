import { Component } from '@angular/core';
import { Club, News} from '../models'
import { ApiService } from '../api.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-club-news',
  templateUrl: './club-news.component.html',
  styleUrls: ['./club-news.component.css']
})
export class ClubNewsComponent {
  club: Club | undefined;
  news_list: News[] = [];

  constructor(private apiService: ApiService, private route: ActivatedRoute){}

  ngOnInit(){
    const routeParams = this.route.snapshot.paramMap;
    const clubIdFromRoute = Number(routeParams.get('id'));

    this.apiService.getClubElemNews(clubIdFromRoute).subscribe((data) => {
      this.news_list = data;
    })
  }
}
