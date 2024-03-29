import {
  BrowserRouter as Router,
  Route,
} from "react-router-dom";
import './App.css';
import './index.css'
import ForAdmissionStudents from "./components/admissionComponents/ForAdmissionStudents";
import EnrollmentBatch from "./components/enrollmentComponents/EnrollmentBatch";
import RenderSchoolYears from "./components/schoolYears/RenderSchoolYears";
import ClassLists from "./components/classListComponents/ClassLists";
import ReToken from "./components/enrollmentComponents/ReToken";
import RenderClassListGrades from "./components/classListComponents/RenderClassListGrades";
import RenderStudentList from "./components/archivesComponents/RenderStudentList";


function App() {
  return (
    <Router>
      <div className="container pt-4">
        <div className="App">
          <Route path="/Registrar/Admission/" exact component={ForAdmissionStudents} />
          <Route path="/Registrar/Enrollment/" exact component={EnrollmentBatch} />
          <Route path="/Registrar/schoolyear/View/" exact component={RenderSchoolYears} />
          <Route path="/Registrar/Classlist/" exact component={ClassLists} />
          <Route path="/Registrar/Enrollment/Re_token/" exact component={ReToken} />
          <Route path="/Registrar/Classlist/Grades/:section_id/" exact component={RenderClassListGrades} />
          <Route path="/Registrar/Archives/" exact component={RenderStudentList} />
        </div>
      </div>
    </Router>
  );
}

export default App;
