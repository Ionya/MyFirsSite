import { Component } from '@angular/core';
import {ApiService} from "../api.service";
import {Ticket, Event} from '../models';

@Component({
  selector: 'app-tickets-list',
  templateUrl: './tickets.component.html',
  styleUrls: ['./tickets.component.css']
})
export class TicketsComponent {

  tickets_list: Ticket[] = [];


  constructor(private api: ApiService) {


  }
  ngOnInit(){
    this.getAllTickets();

  }

  getAllTickets(){
    this.api.getAllTickets().subscribe((data) => {
      this.tickets_list = data;
    })
  }


}
