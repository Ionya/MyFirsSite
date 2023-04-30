import { Component } from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {ApiService} from "../api.service";
import {Ticket} from "../models";

@Component({
  selector: 'app-payment-page',
  templateUrl: './payment-page.component.html',
  styleUrls: ['./payment-page.component.css']
})
export class PaymentPageComponent {

  ticket: Ticket | undefined;

  constructor(private route: ActivatedRoute, private api: ApiService) {

  }
  ngOnInit(){



    this.loadTicket();
  }



  loadTicket(){
    let ticketId: number;
    ticketId = Number(this.route.snapshot.paramMap.get('ticketId'));
    this.api.getTicketById(ticketId).subscribe(
      data => this.ticket = data
    )
  }

}
