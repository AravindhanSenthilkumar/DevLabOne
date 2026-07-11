import { Routes } from '@angular/router';
import { Dashboard } from './dashboard/dashboard';
import { LiveCamera } from './live-camera/live-camera';

export const routes: Routes = [
  { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
  { path: 'dashboard', component: Dashboard },
  { path: 'live-camera', component: LiveCamera },
  { path: '**', redirectTo: 'dashboard' }
];
