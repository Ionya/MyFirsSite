import { Component } from '@angular/core';
import {ApiService} from "../api.service";
import {Event} from "../models"

@Component({
  selector: 'app-events-list',
  templateUrl: './events-list.component.html',
  styleUrls: ['./events-list.component.css']
})
export class EventsListComponent {
  events_list: Event[] = []

  top_list: Event[] = []

  constructor(private api: ApiService) {
    this.getAllEvents()
    this.getTopEvents()
  }


  getAllEvents(){
    this.api.getAllEvents().subscribe(
      data => {
        this.events_list = data;

      },
      error => {
        console.log(error);
      }
    )
  }

  getTopEvents(){
    this.api.getTopEvents().subscribe(
      data => {
        this.top_list = data;

      },
      error => {
        console.log(error);
      }
    )
  }
}
