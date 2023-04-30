export interface News{
  id: number;
  title: string;
  text: string;
  image: string;
  likes: number;
  dislikes: number;
}

export interface Event{
  id: number;
  name: string;
  description: string;
  image: string;
  date_time: Date;
  organizer: string;
  likes: number;
  dislikes: number;
}

export interface Club{
  id: number;
  name: string;
  description: string;
  logo: string;
  likes: number;
  dislikes: number;
}

export interface Location{
  id: number;
  name: string;
  city: string;
  address: string;
  image: string;
  url: string;
}

export interface AuthToken {
  token: string;
}

export interface User{
  user_id: number

  backend_path: string
}

export interface Ticket{
  event: Event
  user: User
  ticket_type: string
  standard_cost: number

}
