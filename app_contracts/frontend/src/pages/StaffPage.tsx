import { Box } from '@mui/material'
import TableComponent from '../components/TableComponent'
import ContractForm from '../components/ContractForm'

const StaffPage = () => {
  return (
    <>
      <Box
        sx={ { display: 'flex', justifyContent: 'center', flexDirection: 'column', alignItems: 'center', gap: '5px' } }>
        <TableComponent/>
        <ContractForm/>
      </Box>
    </>
  )
}

export default StaffPage