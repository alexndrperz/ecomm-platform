import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdminViewComponent } from './view/admin-view/admin-view.component';
import { NotFoundComponent } from './view/not-found/not-found.component';
import { AdminSellersComponent } from './subviews/admin/admin-sellers/admin-sellers.component';

const routes: Routes = [
  {path: 'admin', component:AdminViewComponent, children:[
    {path:'', redirectTo:'sellers', pathMatch:'full'},
    {path:'sellers',component:AdminSellersComponent}
  ]},
  {path: '**', component:NotFoundComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
