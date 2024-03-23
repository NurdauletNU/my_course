import { createBrowserRouter } from 'react-router-dom'

import MainPage from './pages/MainPage'
import StaffPage from './pages/StaffPage'

const status = 'staff'

const router = createBrowserRouter([
  {
    path: '/',
    element: status === 'staff' ? <StaffPage/> : <MainPage/>
  }
])


export default router