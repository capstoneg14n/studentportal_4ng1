import React, {useState, useEffect} from 'react'
import StudentDetailsModal from './enrollmentModals/StudentDetailsModal'
import ImageModal from './enrollmentModals/ImageModal'
import DeniedConfirmationModal from './enrollmentModals/DeniedConfirmationModal';
import MoveToModal from './enrollmentModals/MoveToModal';


export default function EnrolleeDetails({DeniedEnrollee_Handler, enrollment, batchID, move_function}) {
  let [reportCard, setReportCard] = useState('');
  let [studentPicture, setStudentPicture] = useState('');
  let [enrollmentID, setEnrollmentID] = useState(enrollment.id);

  const [studPictModal, setStudPictModal] = useState(false);
  const [studDetailModal, setStudDetailModal] = useState(false);
  const [studCardModal, setReportCardModal] = useState(false);
  const [deniedConfirmationModal, setDeniedConfirmationModal] = useState(false);
  const [moveToModal, setMoveToModal] = useState(false);

  const fetch_reportCard = async (imgurl) => {
    const res = await fetch(imgurl);
    const imageBlob = await res.blob();
    const imageObjectURL = URL.createObjectURL(imageBlob);
    setReportCard(imageObjectURL);
  };

  const fetch_studentPicture = async (imgurl) => {
    const res = await fetch(imgurl);
    const imageBlob = await res.blob();
    const imageObjectURL = URL.createObjectURL(imageBlob);
    setStudentPicture(imageObjectURL);
  };

  useEffect(()=> {
    fetch_reportCard(enrollment.report_card[0].report_card);
    fetch_studentPicture(enrollment.stud_pict[0].user_image);
  }, [enrollment]);

  useEffect(()=> {
    setEnrollmentID(enrollment.id);
  }, [enrollment]);

  return (
    <div className='container'>
      <img src={studentPicture} style={{ width: "20%", height: "20%" }} onMouseMove={() => setStudPictModal(true)} onMouseOut={() => setStudPictModal(false)}/>
      <ImageModal isHovering={studPictModal} img={studentPicture}/>

      <h5 onMouseMove={() => setStudDetailModal(true)} onMouseOut={() => setStudDetailModal(false)}> #{enrollmentID} - {enrollment.applicant}: {enrollment.full_name} - {enrollment.age} </h5>
      <StudentDetailsModal isHovering={studDetailModal} studDetail={enrollment} studpict={studentPicture}/>
      
      <h5 onMouseMove={() => setReportCardModal(true)} onMouseOut={() => setReportCardModal(false)}> Report Card </h5>
      <ImageModal isHovering={studCardModal} img={reportCard}/>

      <button onClick={() => setDeniedConfirmationModal(true)}> Denied </button>
      <DeniedConfirmationModal open={deniedConfirmationModal} closeModalFunc={() => setDeniedConfirmationModal(false)}  DeniedEnrollee_Handler={DeniedEnrollee_Handler} enrollment={enrollment} studentPicture={studentPicture}/>

      <button onClick={() => setMoveToModal(true)}> Move To </button>
      <MoveToModal open={moveToModal} closeModalFunc={() => setMoveToModal(false)} batchID={batchID} enrollmentID={enrollmentID} move_function={move_function}/>
    </div>
  )
}
