import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { BiasharaForm  } from '../models/biashara-form.model';
const apiUrl = 'http://localhost:8000/biashara/';

@Injectable({
  providedIn: 'root'
})
export class BiasharaServiceService {

  constructor(private http: HttpClient) { }
  addResponse(response: BiasharaForm): Observable<BiasharaForm> {
    return this.http.post<BiasharaForm>(apiUrl, response);
  }
}

