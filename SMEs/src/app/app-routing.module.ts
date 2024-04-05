import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BiasharaFormComponent } from './biashara-form/biashara-form.component';

const routes: Routes = [
  { path: 'addresponse', component: BiasharaFormComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
