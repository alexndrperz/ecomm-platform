import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TableComponent } from './components/table/table.component';
import { AdminViewComponent } from './view/admin-view/admin-view.component';
import { NotFoundComponent } from './view/not-found/not-found.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { AdminSellersComponent } from './subviews/admin/admin-sellers/admin-sellers.component';

@NgModule({
  declarations: [
    AppComponent,
    TableComponent,
    AdminViewComponent,
    NotFoundComponent,
    NavbarComponent,
    AdminSellersComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
