import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class ApiConnectService {

  constructor(private http: HttpClient) { }

  fetch(url:string) {
    return this.http.get(url)
  }

  post(url:string, data:any=null){
    return this.http.post(url, data)
  } 
}
