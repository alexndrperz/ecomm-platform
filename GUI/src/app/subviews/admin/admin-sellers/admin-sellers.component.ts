import { HttpRequest } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { map } from 'rxjs/operators';
import { ApiConnectService } from 'src/app/services/api-connect.service';

@Component({
  selector: 'app-admin-sellers',
  templateUrl: './admin-sellers.component.html',
  styleUrls: ['./admin-sellers.component.css']
})
export class AdminSellersComponent implements OnInit{
  constructor(private apiServ:ApiConnectService) {}

  data:any[] = [];
  header:string[]= []

  ngOnInit(): void {
    this.fetchAPI()
  }

  fetchAPI() {
    this.apiServ.fetch(`http://127.0.0.1:8000/sellers/`)
    .pipe(
      map((response:any) => ({
       ...response,
        data:response.data.map((item: any) => ({
        ...item, 
        isCopied:false
       }))  
      }))
      )

    .subscribe((response:any) => {
      console.log(response)
      this.data= response.data
      this.header = ['Id','Nombre','Comisión', 'Ventas','Balance','Opciones']
    })
  }
  

}
