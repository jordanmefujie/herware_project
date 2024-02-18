

import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Login from './components/Authentication/Login';
import Register from './components/Authentication/Register';
import UserProfile from './components/Profile/UserProfile';
import EditProfile from './components/Profile/EditProfile';
import HealthTracker from './components/HealthData/HealthTracker';
import Dashboard from './components/Dashboard/Dashboard';
import EducationalResources from './components/Resources/EducationalResources';
import Forum from './components/Community/Forum';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/login" component={Login} />
          <Route path="/register" component={Register} />
          <Route path="/profile" component={UserProfile} />
          <Route path="/edit-profile" component={EditProfile} />
          <Route path="/health-tracker" component={HealthTracker} />
          <Route path="/dashboard" component={Dashboard} />
          <Route path="/resources" component={EducationalResources} />
          <Route path="/forum" component={Forum} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
