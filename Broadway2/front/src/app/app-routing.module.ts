import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { NewsComponent } from './news/news.component';
import { NewsDetailsComponent } from './news-details/news-details.component';
import { EventsComponent } from './events/events.component';
import { EventsDetailsComponent } from './events-details/events-details.component';
import { HomeComponent } from './home/home.component';
import { ClubsComponent } from './clubs/clubs.component';
import { ClubsDetailsComponent } from './clubs-details/clubs-details.component';
import { ClubEventsComponent } from './club-events/club-events.component';
import { ClubNewsComponent } from './club-news/club-news.component';
import { LocationsComponent } from './locations/locations.component';
import {AppComponent} from "./app.component";
import {EventsListComponent} from "./events-list/events-list.component";
import {ClubsListComponent} from "./clubs-list/clubs-list.component";
import {AboutPageComponent} from "./about-page/about-page.component";
import {ContactPageComponent} from "./contact-page/contact-page.component";
import {NewsListComponent} from "./news-list/news-list.component";
import {TicketsComponent} from "./tickets-list/tickets.component";
import {PaymentPageComponent} from "./payment-page/payment-page.component";
import {LocationsDetailsComponent} from "./locations-details/locations-details.component";

const routes: Routes = [
  // {path: "", component: AppComponent},
  {path: '', component: HomeComponent},
  {path: 'news/:id', component: NewsDetailsComponent},
  {path: 'events-list', component: EventsListComponent},
  {path: 'clubs-list', component: ClubsListComponent},
  {path: 'clubs/:id', component: ClubsDetailsComponent},
  {path: 'clubs/:id/events', component: ClubEventsComponent},
  {path: 'clubs/:id/news', component: ClubNewsComponent},
  {path: 'locations', component: LocationsComponent},
  {path: 'locations/:id', component: LocationsDetailsComponent},
  {path: 'about-page', component: AboutPageComponent},
  {path: 'contact-page', component: ContactPageComponent},
  {path: 'news-list', component: NewsListComponent},
  {path: 'tickets-list', component: TicketsComponent},
  {path: 'payment-page/:ticketId', component: PaymentPageComponent},
  {path: 'events-details/:eventId', component: EventsDetailsComponent}


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
