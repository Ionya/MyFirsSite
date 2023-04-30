import { Component } from '@angular/core';
import { Event } from '../models';
import { ApiService } from '../api.service';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";

@Component({
  selector: 'app-events',
  templateUrl: './events.component.html',
  styleUrls: ['./events.component.css']
})
export class EventsComponent {
  main_events_list: Event[] = [];



  constructor(private apiService: ApiService){}

  ngOnInit(){
    this.getMainEvents();
  }


  getMainEvents = () => {
    this.apiService.getNewEvents().subscribe(
      data => {
        this.main_events_list = data;
      },
      error => {
        console.log(error);
      }
    )
  }
}
