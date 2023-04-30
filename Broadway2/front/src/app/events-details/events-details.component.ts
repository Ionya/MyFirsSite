import { Component, OnInit } from '@angular/core';
import { Event } from '../models';
import { ApiService } from '../api.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-events-details',
  templateUrl: './events-details.component.html',
  styleUrls: ['./events-details.component.css']
})
export class EventsDetailsComponent {
  event: Event | undefined;

  constructor(private apiService: ApiService, private route: ActivatedRoute){

  }

  ngOnInit(){
    const routeParams = this.route.snapshot.paramMap;
    const newsIdFromRoute = Number(routeParams.get('eventId'));

    this.apiService.getEventElement(newsIdFromRoute).subscribe((data) => {
      this.event = data;
    })
  }


  deleteEvent(){
    if(this.event){
      this.apiService.deleteEventElem(this.event.id).subscribe(response => {
        console.log(response);
      })
    }
  }
}
