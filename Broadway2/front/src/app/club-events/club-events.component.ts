import { Component } from '@angular/core';
import { Event, Club } from '../models'
import { ApiService } from '../api.service';
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-club-events',
  templateUrl: './club-events.component.html',
  styleUrls: ['./club-events.component.css']
})
export class ClubEventsComponent {
  club: Club | undefined;
  events_list: Event[] = [];

  constructor(private apiService: ApiService, private route: ActivatedRoute){}

  ngOnInit(){
    const routeParams = this.route.snapshot.paramMap;
    const clubIdFromRoute = Number(routeParams.get('id'));

    this.apiService.getClubElemEvents(clubIdFromRoute).subscribe((data) => {
      this.events_list = data;
    })
  }
}
