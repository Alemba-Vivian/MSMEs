import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { BiasharaFormComponent } from "./biashara-form/biashara-form.component";



@Component({
    selector: 'app-root',
    standalone: true,
    templateUrl: './app.component.html',
    styleUrl: './app.component.css',
    imports: [RouterOutlet, BiasharaFormComponent]
})
export class AppComponent {
  title = 'biashara';
}
