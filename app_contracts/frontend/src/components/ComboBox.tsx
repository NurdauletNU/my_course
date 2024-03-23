import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import { useEffect, useState } from 'react';
import axios from 'axios';

export default function ComboBox() {
  const [data, setData] = useState<string[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  const getData = async () => {
    try {
      const res = await axios.get('http://127.0.0.1:8000/api/agents/');
      setData(res.data.data);
      setLoading(false);
    } catch (error) {
      console.error(error);
      setLoading(false);
    }
  };

  useEffect(() => {
    getData();
  }, []);

  return (
    <>
      {loading ? (
        <div>Загрузка...</div>
      ) : (
        <Autocomplete
          disablePortal
          id="combo-box-demo"
          options={data}
          sx={{ width: 300 }}
          renderInput={(params) => <TextField {...params} label="Agents" />}
        />
      )}
    </>
  );
}
