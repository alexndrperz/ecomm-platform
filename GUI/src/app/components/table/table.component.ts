import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})
export class TableComponent implements OnInit {
  @Input() data:any = [];
  @Input() header:string[] = []
  @Input() seller: boolean = false
  @Output() deltUser: EventEmitter<any> = new EventEmitter()

  copied:boolean = false
  dataHeader:string[] = []
  
  ngOnInit(): void {
  }

  deleteUser(item:any): void {
    this.deltUser.emit(item.id)
  }

   getHeaderOfData() {
    if(this.data && this.data[0] != null) {
      return Object.keys(this.data[0]).filter(key => key !=='isCopied' && key !=='url')
    } else {
      return []
    }
  }
  

  copyLink(row: any) {

    navigator.clipboard.writeText(row.url)
    row.isCopied = true
    setTimeout(()=> {
      row.isCopied = false
    }, 1000)
  }
}
