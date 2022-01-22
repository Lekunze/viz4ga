import * as React from 'react';
import {Header,Heading, Box} from 'grommet';
import ReactTooltip from 'react-tooltip';

function HeadPanel(){
    const label = "Configure optimization parameters for genetic algorith,"
    return(
        <Header background="#2a3142">
            <Box pad="small">
                <Heading margin="none" level={4} data-tip={label} > Configure GA Parameters </Heading>
            </Box>
            <ReactTooltip  place="bottom" multiline={true}/>
        </Header>

    )
}

export default HeadPanel;